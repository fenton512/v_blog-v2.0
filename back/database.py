from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import DeclarativeBase
from config import DATABASE_URL
 
async_engine = create_async_engine(str(DATABASE_URL), echo= True)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

target_metadata = Base.metadata


class DataBase():

    @classmethod
    async def get_async_db(cls) -> AsyncGenerator[AsyncSession, None]:
        async with async_session_maker() as session:
            yield session

