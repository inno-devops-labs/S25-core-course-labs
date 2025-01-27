from fastapi import APIRouter
import datetime
import pytz

router = APIRouter()

@router.get("/msc_time")
async def get_moscow_time() -> dict[str, str]:
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.datetime.now(tz=moscow_tz)
    return {
        "current_time_in_moscow": moscow_time.strftime("%Y-%m-%d %H:%M:%S")
    }