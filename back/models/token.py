from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, ForeignKey, DateTime
from datetime import datetime
from .base import Base


class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    family_id: Mapped[int] = mapped_column(nullable=False)
    token_hash: Mapped[String] = mapped_column(String, index=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)
    expired_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)