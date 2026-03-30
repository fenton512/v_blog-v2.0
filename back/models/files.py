from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from .posts import Post


class File(Base):
    __tablename__ = "files"
    id: Mapped[int] = mapped_column(unique=True, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    type: Mapped[str] = mapped_column(String(7), index=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False, index=True)

    post: Mapped["Post"] = relationship("Post", uselist=False, back_populates="files")