from fastapi import FastAPI, routing
from routes.posts import router as post_router

app = FastAPI()
app.include_router(post_router)

@app.get("/")
async def start_page()-> dict[str, str]:
    return {"message": "hi from root"}
