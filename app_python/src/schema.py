from pydantic import BaseModel


class GetTimeResponse(BaseModel):
    current_time: str
