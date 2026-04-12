import abc
from datetime import datetime
from models import Post as PostModel, File as FileModel, Theme as ThemeModel, User as UserModel, Token as TokenModel, Comment as CommentModel
from typing import cast, TypeVar, Callable, Type, Sequence, TYPE_CHECKING, Any, Tuple, Generic, ClassVar
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from collections.abc import AsyncGenerator
from sqlalchemy import select, update, delete, Select, func
from sqlalchemy.orm import DeclarativeBase, selectinload, Mapped
from config import DATABASE_URL
 

class Base(DeclarativeBase):
    pass


T = TypeVar('T')
B = TypeVar('B', bound=Base)

def singleton(cls: Type[T])-> Callable[..., T]:
    instances: dict[Type[T], object] = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
              instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return cast(Type[T], get_instance )


class DataBase(abc.ABC, Generic[B]):

    async_engine = create_async_engine(str(DATABASE_URL), echo= True)
    async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
    related_model: Type[B] 
    relations: ClassVar[list]

    #add exception if no relation with such attr in args
    def add_lazy_load(self, stmt: Select[Tuple[B]])-> Select[Tuple[B]]:
        return stmt.options(*[selectinload(r) for r in self.relations])
    
    async def get_by_id(self, id: int, session: AsyncSession)-> B:
        stmt = (select(self.related_model)).where(getattr(self.related_model, "id") == id)
        stmt = self.add_lazy_load(stmt) 
        result =  await session.scalars(stmt)
        result = result.first()
        if result is None:
             raise NoEntityException(msg="There is no {B} with such id")
        return result

    async def does_exist(self, session: AsyncSession,  **kwargs) -> B | None:
        filters = [getattr(self.related_model, key) == value for key, value in kwargs.items() if hasattr(self.related_model, key)]

        stmt = select(self.related_model).where(*filters)
        result = await session.scalars(stmt)
        result = result.first()
        # if result is None:
        #     raise NoEntityException
        return result

    async def get_all(self, session: AsyncSession)->Sequence[B]: 
        stmt = select(self.related_model)
        stmt = self.add_lazy_load(stmt).options(selectinload(PostModel.author))
        result = await session.scalars(stmt)
        return result.all()

    async def delete_row(self, session: AsyncSession, id: int|None = None, instance:B|None = None):
        if instance is not None:
            await session.delete(instance)
        elif id is not None:
            stmt = delete(self.related_model).where(getattr(self.related_model, "id") == id)
            await session.execute(stmt)
            await session.commit()
        
    @classmethod
    async def get_async_db(cls) -> AsyncGenerator[AsyncSession, None]:
            async with cls.async_session_maker() as session:
                yield session
    

    @abc.abstractmethod
    async def add_row(self, session: AsyncSession, instance_data: dict[str, Any]) -> B: pass

@singleton
class ThemeDBManager(DataBase[ThemeModel]):
    related_model = ThemeModel
    relations = [
        ThemeModel.posts
    ]
    async def add_row(self, session: AsyncSession, instance_data: dict[str, Any]) -> ThemeModel:
       new_theme = ThemeModel(**instance_data)
       session.add(new_theme) 
       await session.flush()
       return new_theme

    async def update_row(self, session: AsyncSession, **kwargs):
        theme_for_update = await self.does_exist(session, **kwargs)
        if theme_for_update is not None:
            pass
        else:
            raise NoEntityException
        
theme_db_manager = ThemeDBManager()
@singleton
class PostDBManager(DataBase[PostModel]):
    related_model = PostModel
    relations = [
        PostModel.comments, 
        PostModel.files,
        PostModel.groups, 
        PostModel.themes,
        ]
    async def add_row(self, session:AsyncSession, instance_data: dict[str, Any] )->PostModel:
        files: list[FileModel] = []
        themes: list[ThemeModel] = []
        post_attribures = {}
        for key, value in instance_data.items():
            match key:
                case "images_URL" | "voices_URL":
                    for url in value:
                        new_file = (FileModel(url=url, type=f'{key[:key.index('_')-1]}'))
                        files.append(new_file)
                        session.add(new_file)     
                case "themes":
                    for theme_name in value:
                        db_theme = await theme_db_manager.does_exist(session, name = theme_name) 

                        if db_theme is None:
                            new_theme = await theme_db_manager.add_row(session, {"name": theme_name})
                            themes.append(new_theme)  
                            session.add(new_theme)
                        else:
                            themes.append(db_theme)
                case _:
                    post_attribures[key] = value

        id = post_attribures["author"].id
        post_attribures["author_id"] = id
        new_post = PostModel(**post_attribures)
        new_post.author = post_attribures["author"]

        session.add(new_post)
        for file in files:
            new_post.files.append(file)
        for theme in themes:
            new_post.themes.append(theme)
        await session.commit()
        stmt = select(PostModel).where(PostModel.id == new_post.id)
        stmt = self.add_lazy_load(stmt) 
        new_post = await session.scalars(stmt)
        new_post = new_post.first()
        return new_post
        
    async def update_post(self, id: int, new_post_data: dict[str, Any], session: AsyncSession, old_post: PostModel|None = None) -> PostModel:
        try:
            old_post = await self.get_by_id(id, session) if old_post == None else old_post
            new_themes = new_post_data.get("themes")
            old_themes = [theme for theme in old_post.themes if theme.name not in new_themes] #type: ignore
            #removing redandent themes
            for old_theme in old_themes:
                old_post.themes.remove(old_theme)
            if new_themes is not None:
                #adding new theme to the post
                old_theme_names = [theme.name for theme in old_post.themes]
                for theme_name in new_themes:
                    #check if theme is new for post
                    if theme_name not in old_theme_names:
                        db_theme = await theme_db_manager.does_exist(session, name=theme_name)
                        #check if theme is new for db
                        if db_theme is None:
                            db_theme =  await theme_db_manager.add_row(session, {"name": theme_name}) 
                        old_post.themes.append(db_theme)
            for key, value in new_post_data.items():
                if hasattr(old_post, key) and key != "themes":
                    setattr(old_post, key, value)
            old_post.updating_time = datetime.now()
            await session.flush()
            await session.commit()
            return old_post
        except NoEntityException:
            raise NoEntityException
        
    async def delete_post(self, id: int, session: AsyncSession):
        try:
            post = await self.get_by_id(id, session)
            result = session.delete(post)
            await session.commit()
        except NoEntityException as e:
            raise NoEntityException
            
db_post_manager = PostDBManager()

class UserDbManager(DataBase[UserModel]):
    related_model = UserModel
    relations = [
        UserModel.comments, 
        UserModel.groups, 
        UserModel.posts
    ]
    
    async def add_row(self, session:AsyncSession, instance_data: dict[str, Any])-> UserModel:
        password = instance_data["password"]
        instance_data.update({"password": password})
        new_user = UserModel(**instance_data)
        session.add(new_user)
        await session.commit()
        return new_user




db_user_manager = UserDbManager()

@singleton
class CommentDBManager(DataBase[CommentModel]):
    related_model = CommentModel

    async def add_row(self, session: AsyncSession, instance_data: dict[str, Any]) -> CommentModel:
        author: UserModel = instance_data["author"]
        post: PostModel = instance_data["post"]
        model = CommentModel(text=instance_data["text"],
                             author_id=author.id,
                             post_id = post.id)
        session.add(model)
        await session.commit()
        return model

db_comment_manager = CommentDBManager()
@singleton
class TokenDbManager(DataBase[TokenModel]):
    related_model = TokenModel
    async def add_row(self, session: AsyncSession, instance_data: dict[str, Any]) -> TokenModel:
        new_token = TokenModel(**instance_data)
        session.add(new_token)
        await session.commit()
        return new_token

    async def block_session(self, session: AsyncSession, family_id: int)->None:
        stmt = (
            update(self.related_model)
            .where(self.related_model.family_id == family_id)
            .values(is_active = False)
        )
        await session.execute(stmt)
        await session.commit()
        

    async def get_next_family_id(self, session: AsyncSession) -> int:
        stmt = select(func.max(self.related_model.family_id))
        result = await session.scalars(stmt)
        result = result.first()
        if result is None:
            stmt = select(func.count(self.related_model.id))
            result = await session.scalars(stmt)
            result = result.first()
            if result == 0:
                return 1 
            else:
                raise NoEntityException(msg="there are tokens in db, but result is None")
        return cast(int, result)

    async def make_inactive(
                            self, 
                            session: AsyncSession,
                            id: int|None = None, 
                            instanse: TokenModel|None = None
                            ) -> None:
        if instanse is not None:
            instanse.is_active = False
        elif id is not None:
            instanse = await self.get_by_id(id, session)
            instanse.is_active = False
        else:
            raise BadAttributeException(id=id, instanse=instanse)

db_token_manager = TokenDbManager()


class NoEntityException(Exception):
    def __init__(self, msg="There is no instance with such attribute", **kwargs) -> None:
        super().__init__(msg)
        self.attributes = kwargs
        self.msg = msg
    def __str__(self) -> str:
        return f'{self.msg}: {self.attributes}'

class BadAttributeException(Exception):
    def __init__(self, msg = "function has no needed attributes", **kwargs) -> None:
        super().__init__(msg)
        self.attributes = kwargs
        self.msg = msg
    def __str__(self) -> str:
        return f'{self.msg}: {self.attributes}'