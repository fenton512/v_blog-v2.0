import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://Vector:33Victor@localhost:5432/vector_blog")
SECRET_KEY_ACCESS = os.getenv("SECRET_KEY_ACCESS")
SECRET_KEY_REFRESH = os.getenv("SECRET_KEY_REFRESH")
ALGORITH = os.getenv("ALGORITHM")