from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated

from datetime import datetime

CreationTime = Annotated[datetime, Field (default_factory=datetime.now, description="Time of creation")]
UpdationTime = Annotated[datetime, Field(default=None, description="The time of updating")]

class BasePost(BaseModel):
    text: str = Field(..., min_length=15, description="The text content of the post")
    images_URL: list[str] = Field(default_factory=list, description="URL of the photos are attached to the post") 
    voices_URL: list[str] = Field(default_factory=list, description="URL of the voices are attached to the post")
    #add default theme
    themes: list[str] = Field(..., description="The post's name")
    heshtags: list[str] = Field(default_factory=list, description="Hashtags of the post")

    model_config = ConfigDict(extra="forbid")

class PostResponse(BasePost):
    id: int  = Field(..., ge=1, description="The identifier for post")
    comments: list["BaseComment"] = Field (default_factory=list, description="The comments of the post")
    created_at: "CreationTime"
    updated_at: UpdationTime

    model_config = ConfigDict(from_attributes=True)
    
class PostPut(BaseModel):
    text: str|None = Field(default=None, min_length=15, description="The text content of the post")
    images_URL: list[str]|None = Field(None, description="URL of the photos are attached to the post") 
    voices_URL: list[str]|None = Field(None, description="URL of the voices are attached to the post")
    themes: list[str]|None = Field(default=None, description="The post's name")
    heshtags: list[str]|None = Field(None, description="Hashtags of the post")

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

class Author(BaseModel):
    name: str = Field(..., min_length=3)
    id: int = Field(..., ge=1)

