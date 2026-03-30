from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from shemas import BaseComment, CommentResponse, UserComment, UserMainResponse
from .users import get_current_user
from database import DataBase, db_post_manager, db_comment_manager, NoEntityException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import cast
router = APIRouter(prefix= "/comments", tags=["comments"])

@router.post("/{post_id}", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def write_comment(post_id: int, 
                     new_comment: BaseComment, 
                     user:UserMainResponse  = Depends(get_current_user),
                     session: AsyncSession = Depends(DataBase.get_async_db))->CommentResponse:
    try:
        post = await db_post_manager.get_by_id(post_id, session)
        author = UserComment(
            nickname=user.nickname,
            id=user.id,
            avatar_url=user.avatar_url
        )
        data = {"post": post,
                "text": new_comment.text,
                "author": author}
        new_comment = await db_comment_manager.add_row(session, instance_data=data)
        return cast(CommentResponse, new_comment)

    except NoEntityException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) 
    
@router.patch("/{post_id}/{comment_id}")
async def change_comment(post_id: int, 
                         comment_id: int,
                         new_comment: BaseComment,
                         user: UserMainResponse = Depends(get_current_user), 
                         session: AsyncSession = Depends(DataBase.get_async_db))->CommentResponse:
    old_comment = await db_comment_manager.does_exist(session, id = comment_id, post_id = post_id)
    if old_comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="There is no such comment in this post")
    elif old_comment.author_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You are not the author of this comment")
    old_comment.updating_time = datetime.now()
    old_comment.text = new_comment.text
    await session.commit()
    return cast(CommentResponse, old_comment)


@router.delete("/{post_id}/{comment_id}")
async def delete_comment(post_id: int,
                         comment_id: int,
                         user: UserMainResponse = Depends(get_current_user),
                         session: AsyncSession = Depends(DataBase.get_async_db))->dict[str, str]:
    post = await db_comment_manager.does_exist(session, id=comment_id, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="There is no such comment in this post")
    elif user.id != post.author_id and user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You are not the author of this comment")
    await db_comment_manager.delete_row(session, id=comment_id)
    return {"message": "deletion complite!"}

