from fastapi import APIRouter
from datetime import datetime
from pytz import timezone

from src.utils.visits_manager import inc_visits


router = APIRouter()

@router.get("/")
async def read_time():
    inc_visits()
    moscow = timezone('Europe/Moscow')
    current_time = datetime.now(moscow).strftime("%Y-%m-%d %H:%M:%S")
    return {"Moscow Time": current_time}
