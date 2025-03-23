from pathlib import Path


class Config:
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    TIMEZONE: str = "Europe/Moscow"
    TEMPLATES_DIR: Path = Path("templates")
