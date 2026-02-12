from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Text, ForeignKey, DateTime
from datetime import datetime
from database import Base
from typing import TYPE_CHECKING

from .secondary_tables import themes_in_post
if TYPE_CHECKING:
    from .themes import Theme
    from .comments import Comment
    from .users import User
    from .files import File

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, index=True)
    updating_time: Mapped[datetime] = mapped_column(DateTime, default=None)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)


    files: Mapped[list["File"]] = relationship("File", back_populates="post", cascade="all, delete-orphan")
    themes: Mapped[list["Theme"]] = relationship("Theme", secondary=themes_in_post, back_populates="posts")
    author: Mapped["User"] = relationship("User", uselist=False, back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
