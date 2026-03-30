from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Table, Column, Boolean
from .secondary_tables import themes_in_post
from .posts import Post

class Theme(Base):
    __tablename__ = "themes"
    id: Mapped[int] = mapped_column(unique=True, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(index=True, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    posts: Mapped[list["Post"]] = relationship("Post", secondary=themes_in_post, back_populates="themes")