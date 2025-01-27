from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .routes import router

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(router)
