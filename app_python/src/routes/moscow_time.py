from fastapi import APIRouter
from datetime import datetime
from pytz import timezone

router = APIRouter()

@router.get("/")
async def read_time():
    moscow = timezone('Europe/Moscow')
    current_time = datetime.now(moscow).strftime("%Y-%m-%d %H:%M:%S")
    return {"Moscow Time": current_time}
