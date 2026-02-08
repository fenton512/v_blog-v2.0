from fastapi import APIRouter, HTTPException, status
from shemas import BasePost as PostCreate, PostPut, PostResponse
router = APIRouter(prefix="/posts", tags=["posts"])


fake_db:dict[int, PostResponse] = {}
@router.get("/", response_model=dict[int, PostResponse])
def get_all_posts()->dict[int, PostResponse] :
    return fake_db

@router.get("/{post_id}")
def get_post_by_id(post_id: int) -> PostResponse:
    return fake_db[post_id]

@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate)-> PostResponse:
    new_id = len(fake_db) + 1
    new_post = PostResponse(**post.model_dump(), id=new_id)
    fake_db.update({new_id: new_post})
    return new_post

    
@router.put("/{post_id}")
def update_post(post_id: int, new_post: PostPut)->PostResponse:
    new_post_dict = new_post.model_dump(exclude_defaults=True)
    old_post = fake_db.get(post_id)
    if old_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    for key, value in new_post_dict.items():
        if hasattr(old_post, key):
            setattr(old_post, key, value)
    return old_post
@router.delete("/{post_id}")
def delete_post(post_id: int)-> dict[str, str]:
    fake_db.pop(post_id)
    return {"message": "deleted"}

