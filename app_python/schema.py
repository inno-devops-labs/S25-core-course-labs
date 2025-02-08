from pydantic import BaseModel
import datetime

class GetTimeResponse(BaseModel):
    current_time: str
