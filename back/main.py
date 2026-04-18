from fastapi import FastAPI, routing
from routes.posts import router as post_router
from routes.users import router as token_router
from routes.comments import router as comment_router
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
origins = [
    "http://localhost:8080",
    "http://193.108.113.5",
    "vector-blog.ru"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["App-Error-Code"]
)
app.include_router(post_router)
app.include_router(token_router)
app.include_router(comment_router)


@app.get("/")
async def start_page()-> dict[str, str]:
    return {"message": "hi from root"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)