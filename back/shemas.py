from pydantic import BaseModel, Field, ConfigDict, EmailStr, field_validator
from typing import Annotated

from datetime import datetime

from fastapi import HTTPException, status
CreationTime = Annotated[datetime, Field (default_factory=datetime.now, description="Time of creation")]
UpdationTime = Annotated[datetime, Field(default=None, description="The time of updating")]

class BasePost(BaseModel):
    text: str = Field(..., min_length=15, description="The text content of the post")
    images_URL: list[str] = Field(default_factory=list, description="URL of the photos are attached to the post") 
    voices_URL: list[str] = Field(default_factory=list, description="URL of the voices are attached to the post")
    #add default theme
    themes: list[str] = Field(..., description="The post's name")
    groups: list[str] = Field(default_factory=list, description="The list of groupes that can see that post")

    model_config = ConfigDict(extra="forbid")

class PostResponse(BasePost):
    id: int  = Field(..., ge=1, description="The identifier for post")
    comments: list["BaseComment"] = Field (default_factory=list, description="The comments of the post")
    created_at: "CreationTime"
    updated_at: UpdationTime

    model_config = ConfigDict(from_attributes=True)
    
class PostPut(BaseModel):
    text: str|None = Field(default=None, min_length=15, description="The text content of the post")
    files_URL: list[str]|None = Field(None, description="URL of the photos are attached to the post") 
    themes: list[str]|None = Field(default=None, description="The post's name")

    model_config = ConfigDict(extra="forbid")


class BaseComment(BaseModel):
    text: str = Field(..., min_length=4, max_length=220, description="The content of comment")

class CommentResponse(BaseComment):
   id: int = Field(..., ge=1) 
   author_id: int = Field(..., ge=1)
   post_id: int = Field(..., ge=1)
   created_at: CreationTime
   updated_at: UpdationTime 

class CommentEdit(BaseComment):
    text: str = Field(..., min_length=4, description="The author of the comment")

class BaseUser(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    nickname: str = Field(..., min_length=3)

class UserResponse(BaseUser):
    id: int = Field(..., ge=1)
    role: str = Field()
    avatar_URL: str = Field(...)
    description: str | None = Field(default=None)
    group: list[str] | None = Field(default_factory=list)

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

