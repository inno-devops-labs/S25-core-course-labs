import pytz
from datetime import datetime
from schemas import TimeSerializer
from fastapi import APIRouter

router = APIRouter(prefix="/time", tags=["Time"])


@router.get("/", summary="MSK time", response_model=TimeSerializer)
async def get_time():
    tz = pytz.timezone('Europe/Moscow')
    return {"time": str(datetime.now(tz))}
