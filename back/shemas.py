from pydantic import BaseModel, Field, ConfigDict, EmailStr, field_validator, SecretStr
from typing import Annotated

from datetime import datetime

from fastapi import HTTPException, status
CreationTime = Annotated[datetime, Field (default_factory=datetime.now, description="Time of creation")]
UpdationTime = Annotated[datetime|None, Field(default=None, description="The time of updating")]

class BasePost(BaseModel):
    text: str = Field(..., min_length=15, description="The text content of the post")
    images_URL: list[str] = Field(default_factory=list, description="URL of the photos are attached to the post") 
    voices_URL: list[str] = Field(default_factory=list, description="URL of the voices are attached to the post")
    #add default theme
    themes: list[str] = Field(..., description="The post's heshtags like indicator")
    groups: list[str] = Field(default_factory=list, description="The list of groupes that can see that post")

    model_config = ConfigDict(extra="forbid")

class PostResponse(BasePost):
    id: int  = Field(..., ge=1, description="The identifier for post")
    comments: list["CommentResponse"] = Field (default_factory=list, description="The comments of the post")
    created_at: "CreationTime"
    updated_at: UpdationTime
    author: "UserComment"

    model_config = ConfigDict(from_attributes=True)
    @classmethod
    def to_pd_model(cls, post):
        themes = [theme.name for theme in post.themes]
        author = UserComment(id=post.author_id, avatar_url= post.author.avatar_url, nickname=post.author.nickname)
        return cls(
            id = post.id,
            comments = post.comments,
            themes = themes,
            created_at = post.creation_time,
            updated_at = post.updating_time,
            text = post.text,
            author = author
        )


class PostPut(BaseModel):
    text: str|None = Field(default=None, min_length=15, description="The text content of the post")
    files_URL: list[str]|None = Field(None, description="URL of the photos are attached to the post") 
    themes: list[str]|None = Field(default=None, description="The post's name")
    groups: list[str] = Field(default_factory=list, description="The list of groupes that can see that post")

    model_config = ConfigDict(extra="forbid")


class BaseComment(BaseModel):
    text: str = Field(..., min_length=4, max_length=220, description="The content of comment")

class CommentResponse(BaseComment):
    id: int = Field(..., ge=1) 
    author: "UserComment" = Field(...)
    created_at: CreationTime
    updated_at: UpdationTime 

    model_config = ConfigDict(from_attributes=True)
class CommentEdit(BaseComment):
    text: str = Field(..., min_length=4, description="The text of the comment")

class RefreshRequest(BaseModel):
    refresh_token: str

class RefreshResponse(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str

class NewUserResponse(BaseModel):
    id: int = Field(..., ge=1)
    token: RefreshResponse
    email: EmailStr
    nickname: str

    model_config = ConfigDict(from_attributes=True)

class BaseUser(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    nickname: str = Field(..., min_length=3)

class UserComment(BaseModel):
    nickname: str = Field(...)
    id: int = Field(..., ge=1)
    avatar_url: str|None = Field(default=None)

    model_config = ConfigDict(from_attributes=True)

class UserMainResponse(BaseModel):
    id: int = Field(..., ge=1)
    email: EmailStr= Field(...)
    nickname: str = Field(...)
    role: str = Field(...)
    avatar_url: str|None = Field(default=None)
    description: str | None = Field(default=None)

    model_config = ConfigDict(from_attributes=True)
    @field_validator("role")
    @classmethod
    def check_accepted_roles(cls, value: str):
        roles =  ["admin", "writer", "reader"]
        if value.lower() in roles:
            return value
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No such role")

class UserPut(BaseModel):
    email: str | None = Field(default=None)
    password: str | None = Field(default=None)
    nickname: str | None = Field(default=None)
    avatar_URL: str | None = Field(default=None)
    desctiption: str | None = Field(default=None)



