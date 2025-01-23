from fastapi import FastAPI

from .config import settings
from .routes import router

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
)
app.include_router(router)
