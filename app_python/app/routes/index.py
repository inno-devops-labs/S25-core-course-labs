from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from utils.time_helper import get_moscow_time
from utils.config import Config

router = APIRouter()
templates = Jinja2Templates(directory=str(Config.TEMPLATES_DIR))


@router.get('/')
async def get_current_time(request: Request):
    """Return current time in Moscow timezone."""

    curr_time = get_moscow_time()
    return templates.TemplateResponse(
        request,
        "index.html",
        {"current_time": curr_time}
    )
