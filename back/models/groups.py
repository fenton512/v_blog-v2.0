from .users import User
from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Table, Column, Text
from .secondary_tables import users_in_group, posts_in_group
from .posts import Post


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)

    users: Mapped[list["User"]] = relationship("User", secondary=users_in_group, back_populates="groups")
    posts: Mapped[list["Post"]] = relationship("Post", secondary=posts_in_group, back_populates="groups")