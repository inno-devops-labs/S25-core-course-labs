from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from utils.time_helper import get_moscow_time
from utils.config import Config
import os
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=str(Config.TEMPLATES_DIR))


def get_visits_file_path():
    file_path = os.environ.get('VISITS_FILE', './app/data/visits.txt')
    # Ensure directory exists
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    return file_path


def get_visits():
    try:
        file_path = get_visits_file_path()
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return int(f.read().strip() or '0')
        return 0
    except (FileNotFoundError, ValueError):
        return 0


def increment_visits():
    visit_count = get_visits() + 1
    with open(get_visits_file_path(), 'w') as f:
        f.write(str(visit_count))
    return visit_count


@router.get('/')
async def get_current_time(request: Request):
    """Return current time in Moscow timezone."""

    curr_time = get_moscow_time()
    increment_visits()
    return templates.TemplateResponse(
        request,
        "index.html",
        {"current_time": curr_time}
    )


@router.get('/visits')
async def show_visits():
    increment_visits()
    visits = get_visits()
    return {"visits": visits}
