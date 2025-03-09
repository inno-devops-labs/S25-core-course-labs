from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import pytz
from pathlib import Path
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

current_dir = Path(__file__).parent
templates = Jinja2Templates(directory=str(current_dir.parent / "templates"))
app.mount("/static", StaticFiles(directory=str(current_dir.parent / "static")),
          name="static")


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
    return templates.TemplateResponse(
        request,
        "index.html",
        {"current_time": current_time}
    )

Instrumentator().instrument(app).expose(app, endpoint="/metrics")
