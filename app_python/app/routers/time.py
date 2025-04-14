from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz

router = APIRouter()

from pathlib import Path

# using relative pathes (thanks to pytest)
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/")
async def root(request: Request):
    """Default page with the current MSK time (UTC+3)"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "moscow_time": moscow_time}
    )

@router.get("/time")
async def get_time():
    """Returns the current MSK time (UTC+3)"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    return {"time": datetime.now(moscow_tz).strftime('%H:%M:%S')}