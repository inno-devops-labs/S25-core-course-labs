from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    TIMEZONE: str = "Europe/Moscow"
    TEMPLATES_DIR: Path = Path("../templates")


settings = Settings()
