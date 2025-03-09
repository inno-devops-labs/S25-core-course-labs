from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """Application settings."""
    APP_TITLE: str = "Moscow Time Display"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    TIMEZONE: str = "Europe/Moscow"
    TEMPLATES_DIR: Path = Path(__file__).parent / "templates"
    
    class Config:
        env_file = ".env"

settings = Settings() 