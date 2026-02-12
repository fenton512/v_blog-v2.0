from database import Base, target_metadata
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Table, Column, Integer


themes_in_post = Table(
    "themes_in_post",
    target_metadata,
    Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, index=True),
    Column("theme_id", Integer, ForeignKey("themes.id", ondelete="CASCADE"), primary_key=True, index=True)
)

users_in_group = Table(
    "users_in_group",
    target_metadata,
    Column("user_id", Integer,  ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, index=True),
    Column("groupe_id", Integer, ForeignKey("groupes.id", ondelete="CASCADE"), primary_key=True, index=True)
)

posts_in_group = Table(
    "posts_in_group",
    target_metadata, 
    Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, index=True),
    Column("group_id", Integer,ForeignKey("groupes.id", ondelete="CASCADE"), primary_key=True, index=True),
)