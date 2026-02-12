from .users import User
from datetime import datetime
from database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Table, Column, Text, DateTime
from .secondary_tables import themes_in_post
from .posts import Post

class Comment(Base):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, index=True)
    updating_time: Mapped[datetime] = mapped_column(DateTime, default=None)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), index=True)

    author: Mapped["User"] = relationship("User", uselist=False)
    post: Mapped["Post"] = relationship("Post", uselist=False)