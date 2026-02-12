from datetime import datetime
from database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import String, ForeignKey, Table, Column, Text, Boolean, event, update

from enum import Enum
from typing import TYPE_CHECKING

from .secondary_tables import users_in_group
if TYPE_CHECKING:
    from .posts import Post
    from .groupes import Group
    from .comments import Comment
    from .users import User


    
class Roles(Enum):
    ADMIN = "admin"
    WRITER = "writer"
    READER = "reader"

class User(Base):

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    nickname: Mapped[str] = mapped_column(String(15), unique=True, index=True)
    role: Mapped[Roles] = mapped_column(String(7))
    password: Mapped[str] = mapped_column(String, unique=True)
    avatar_url: Mapped[str] = mapped_column(String(120))
    desctiption: Mapped[str] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, index=True, nullable=False)

    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")
    groups: Mapped[list["Group"]] = relationship("Groupe", back_populates="users", secondary=users_in_group)
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="author" )
# event listener for deletion User
# when User is deleted, we change it's flag
@event.listens_for(Session, "before_flush")
def soft_delete(session: AsyncSession, flush_context, instances):
    for obj in list(session.deleted):
        if isinstance(obj, User):
            session.deleted.remove(obj)
            obj.is_active = False
            session.add(obj)
           