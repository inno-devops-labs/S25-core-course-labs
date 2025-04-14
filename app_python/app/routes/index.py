from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
from config import settings

router = APIRouter()
templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))


@router.get('/')
async def get_current_time(request: Request):
    """Return current time in Moscow timezone."""

    moscow_timezone = pytz.timezone(settings.TIMEZONE)
    curr_time = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "current_time": curr_time}
    )
