from fastapi import Depends, HTTPException, status, APIRouter, Form, Response, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from database import DataBase, db_user_manager, NoEntityException, db_token_manager, BadAttributeException
from pydantic import SecretStr
from shemas import NewUserResponse, BaseUser as NewUser, UserMainResponse, RefreshResponse, RefreshRequest
from secure.token_auth import create_access_token, hash_password, verify_password, oauth2_scheme, SECRET_KEY_ACCESS, ALGORITH, SECRET_KEY_REFRESH, hash_ref_token, create_refresh_token
import jwt
from models import User as UserModel, Post as PostModel, Token as TokenModel
from enum import Enum
from datetime import datetime

router = APIRouter(prefix="/users", tags=["users"])

class Role(Enum):
    ADMIN = "admin"
    WRITER = "writer"
    READER = "reader"

expired_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token has expired",
    headers={
        "WWW-Authenticate": "Bearer",
        "App-Error-Code": "TOKEN EXPIRED"
        }
    )

credental_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentals",
    headers={"WWW-Authenticate": "Bearer"}
)

invalid_role_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="This feature is not abaliable for you"
)

def need_admin_permission(token: str = Depends(oauth2_scheme))->None:
    if not token:
        raise expired_token_exception
    try:
        payload = jwt.decode(token, SECRET_KEY_ACCESS, algorithms=[ALGORITH]) #type: ignore
        role: str = payload["role"]
        if not role == Role.ADMIN.value:
            raise invalid_role_exception
    except jwt.DecodeError:
        raise credental_exception
    except jwt.ExpiredSignatureError:
        raise expired_token_exception


def need_writer_permission(token: str = Depends(oauth2_scheme))->None:
    if not token:
        raise expired_token_exception
    try:
        payload = jwt.decode(token, SECRET_KEY_ACCESS, algorithms=[ALGORITH])#type: ignore
        role: str = payload["role"]
        if not (role == Role.WRITER.value or role == Role.ADMIN.value):
            raise invalid_role_exception
    except jwt.DecodeError:
        raise credental_exception
    except jwt.ExpiredSignatureError:
        raise expired_token_exception

def is_author(post: PostModel, token: str):
    payload = jwt.decode(token, SECRET_KEY_ACCESS, algorithms=[ALGORITH])#type: ignore
    return post.author_id == payload["sub"]


def build_token_dict(family_id: int, refresh_token: str, user_id: int, expired_at: datetime):
    return {
            "user_id": user_id,
            "family_id": family_id,
            "token_hash": hash_ref_token(refresh_token),
            "expired_at": expired_at
            }


@router.post("/token", status_code=status.HTTP_201_CREATED)
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(DataBase.get_async_db)) -> dict[str, str]:
    email = form_data.username
    password = form_data.password

    user = await db_user_manager.does_exist(session, email = email)
    if (user is None) or (not verify_password(password, user.password)):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Email or password is not correct", headers={"WWW-Authenticate": "Bearer"})

    data = {"sub": str(user.id), "role": user.role, "email": user.email}
    refresh_token, expire =  create_refresh_token(data).values()
    family_id = await db_token_manager.get_next_family_id(session)
    await db_token_manager.add_row(session, instance_data=build_token_dict(family_id, refresh_token, user.id, expire))
    result = {"access_token": create_access_token(data = data), "refresh_token": refresh_token, "token_type":"bearer"}
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, path="/users/refresh", samesite='strict')
    return result
    



@router.post("/refresh", status_code=status.HTTP_201_CREATED)
async def refresh_access_token(response: Response, session: AsyncSession = Depends(DataBase.get_async_db), refresh_token: str = Cookie(...))-> dict: #type: ignore
    # refresh_token = refresh_token.refresh_token
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY_REFRESH, algorithms=[ALGORITH] ) #type: ignore
        id, email = payload["sub"], payload["email"]
        user = await db_user_manager.does_exist(session, id = int(id), email = email)
        if user is None:
            raise credental_exception
        token = await db_token_manager.does_exist(session, token_hash = hash_ref_token(refresh_token))
        if token is None:
            raise credental_exception
        elif token.is_active == False:
            await db_token_manager.block_session(session, token.family_id)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Session is canceled due to suspect activity"
                                )
        elif token.is_active == True:
            payload.pop("exp")
            await db_token_manager.make_inactive(session=session, instanse=token)
            new_refresh_token, expire = create_refresh_token(payload).values()
            family_id = token.family_id            
            await db_token_manager.add_row(session, instance_data=build_token_dict(family_id, new_refresh_token, user.id, expire))
            response.set_cookie(key="refresh_token", value=new_refresh_token, httponly=True, path="/users/refresh", samesite='strict')
            result = {"access_token": create_access_token(payload), "refresh_token": new_refresh_token,"token_type":"bearer"}
            return result
    except jwt.ExpiredSignatureError:
        raise expired_token_exception
    except (jwt.PyJWTError, jwt.DecodeError): 
        raise credental_exception
    except BadAttributeException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))




@router.get("/me")
async def get_current_user(session: AsyncSession = Depends(DataBase.get_async_db), token: str = Depends(oauth2_scheme))->UserMainResponse:
    try:
        payload = jwt.decode(token, SECRET_KEY_ACCESS, algorithms=[ALGORITH]) #type: ignore
        id: int = int(payload["sub"])
        if id is None:
            raise credental_exception
        user = await db_user_manager.get_by_id(id, session)
    except jwt.ExpiredSignatureError:
        raise expired_token_exception
    except (jwt.PyJWKError, NoEntityException):
        raise credental_exception
    return user








    
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NewUserResponse)
async def register(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), nickname: str = Form(...), session: AsyncSession = Depends(DataBase.get_async_db))-> NewUserResponse:
    print(1)
    check_user = await db_user_manager.does_exist(session= session, email = form_data.username)
    if check_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with such email already exist")
    hashed_password = hash_password(form_data.password)
    instance_data = {
        "email": form_data.username,
        "password": hashed_password,
        "nickname": nickname
    }
    new_user = await db_user_manager.add_row(session, instance_data=instance_data)
    data = {"sub": str(new_user.id), "role": new_user.role, "email": new_user.email}
    user_data = {
        "email" : new_user.email,
        "id" : new_user.id,
        "nickname" : new_user.nickname
    }
    refresh_token, expire =  create_refresh_token(data).values()
    family_id = await db_token_manager.get_next_family_id(session)
    await db_token_manager.add_row(session, instance_data=build_token_dict(family_id, refresh_token, new_user.id, expire))
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, path="/users/refresh", samesite='strict')
    user_response = NewUserResponse(token = RefreshResponse(access_token=create_access_token(data=data), refresh_token=refresh_token, token_type="bearer"), **user_data) #type: ignore
    return user_response
