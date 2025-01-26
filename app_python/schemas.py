from pydantic import BaseModel


class TimeSerializer(BaseModel):
    time: str
