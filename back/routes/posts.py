from fastapi import APIRouter, HTTPException, status, Depends

from typing import cast
from shemas import BasePost as PostCreate, PostPut, PostResponse, UserMainResponse
from database import DataBase, db_post_manager, NoEntityException
from sqlalchemy.ext.asyncio import AsyncSession
from .users import need_admin_permission, need_writer_permission, oauth2_scheme, get_current_user, is_author
router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/", response_model=list[PostResponse])
async def get_all_posts(session: AsyncSession = Depends(DataBase.get_async_db))->list[PostResponse] :
    posts = await db_post_manager.get_all(session)
    posts = map(PostResponse.to_pd_model, posts)
    return cast(list[PostResponse], posts) 

@router.get("/{post_id}")
async def get_post_by_id(post_id: int, session: AsyncSession = Depends(DataBase.get_async_db)) -> PostResponse:
    try:
        return PostResponse.to_pd_model(await db_post_manager.get_by_id(post_id, session))
    except NoEntityException as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=e.msg)
        

@router.post("/", dependencies=[Depends(need_writer_permission)])
async def create_post(post: PostCreate, session: AsyncSession = Depends(DataBase.get_async_db), user: UserMainResponse = Depends(get_current_user))-> PostResponse:

    new_post =(post.model_dump(exclude_defaults=True))
    new_post.update({"author": user})
    db_post = await db_post_manager.add_row(session, new_post)
    return PostResponse.to_pd_model(db_post)

    
@router.patch("/{post_id}", dependencies=[Depends(need_writer_permission)])
async def update_post(post_id: int, new_post: PostPut, session: AsyncSession = Depends(DataBase.get_async_db), token: str = Depends(oauth2_scheme))->PostResponse:
    old_post = await db_post_manager.get_by_id(post_id, session)
    if not is_author(old_post, token):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not the author of this post")
    new_post_dict = new_post.model_dump(exclude_defaults=True)
    try:
        new_post = await db_post_manager.update_post(post_id, new_post_dict, session)
        return PostResponse.to_pd_model(new_post)
    except NoEntityException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.msg)

@router.delete("/{post_id}")
async def delete_post(post_id: int, session: AsyncSession = Depends(DataBase.get_async_db))-> dict[str, str]:
    try:
        await db_post_manager.delete_post(post_id, session)
    except NoEntityException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.msg)
    return {"message": "deleted"}

