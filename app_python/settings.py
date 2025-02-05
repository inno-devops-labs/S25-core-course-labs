import os

APP_HOST: str = os.environ.get("APP_HOST", "127.0.0.1")
APP_PORT: int = os.environ.get("APP_PORT", 8000)
