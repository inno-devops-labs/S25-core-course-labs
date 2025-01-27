from datetime import datetime

import pytz
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .config import settings

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    curr_time = datetime.now(pytz.timezone(settings.TIMEZONE))
    formatted_time = curr_time.strftime(settings.DATETIME_FORMAT)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "timezone": settings.TIMEZONE,
            "formatted_time": formatted_time,
        },
    )
