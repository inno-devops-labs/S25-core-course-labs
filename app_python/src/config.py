from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = "Moscow Time Displayer"
    APP_VERSION: str = "0.1.0"

    TIMEZONE: str = "Europe/Moscow"
    DATETIME_FORMAT: str = "%d/%m/%Y %H:%M:%S"


settings = Settings()
