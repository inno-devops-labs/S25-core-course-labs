from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import pytz
from pathlib import Path
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import os

app = FastAPI()

current_dir = Path(__file__).parent
templates = Jinja2Templates(directory=str(current_dir.parent / "templates"))
app.mount("/static", StaticFiles(directory=str(current_dir.parent / "static")),
          name="static")
visits_file = Path("/app/data/visits.txt")

if not visits_file.exists() and os.access(visits_file.parent, os.W_OK):
    visits_file.parent.mkdir(parents=True, exist_ok=True)
    visits_file.write_text("0")
elif not os.access(visits_file.parent, os.W_OK):
    print(
        f"Warning: No write permission for {visits_file.parent}.")


def get_visits_count() -> int:
    if not visits_file.exists():
        return 0
    try:
        with visits_file.open("r") as f:
            return int(f.read().strip())
    except (ValueError, FileNotFoundError):
        return 0


def increment_visits_count():
    count = get_visits_count() + 1
    if os.access(visits_file.parent, os.W_OK):
        with visits_file.open("w+") as f:
            f.write(str(count))
    return count


class TimeData(BaseModel):
    time: str
    timestamp: float


@app.get("/api/moscow_time")
async def get_moscow_time() -> TimeData:
    moscow_tz = pytz.timezone('Europe/Moscow')
    return TimeData(
        time=datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S"),
        timestamp=datetime.now(moscow_tz).timestamp()
    )


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:
    current_time = await get_moscow_time()
    increment_visits_count()
    return templates.TemplateResponse(
        request,
        "index.html",
        {"current_time": current_time}
    )


@app.get("/visits", response_class=HTMLResponse)
async def get_visits(request: Request) -> HTMLResponse:
    increment_visits_count()
    visits = get_visits_count()
    return templates.TemplateResponse(
        request,
        "visits.html",
        {"visits": visits}
    )

Instrumentator().instrument(app).expose(app, endpoint="/metrics")
