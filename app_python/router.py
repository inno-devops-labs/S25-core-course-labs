from fastapi import APIRouter
from schema import GetTimeResponse
import datetime
import pytz

router = APIRouter()

@router.get("/msc_time")
async def get_moscow_time() -> GetTimeResponse:
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.datetime.now(tz=moscow_tz)
    return GetTimeResponse(current_time=moscow_time.strftime("%Y-%m-%d %H:%M:%S"))
