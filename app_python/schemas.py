import datetime

from pydantic import BaseModel, Field


class TimeResponse(BaseModel):
    time: datetime.datetime = Field(..., description="Текущее время по МСК")
