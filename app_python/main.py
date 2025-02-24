"""Module with FastAPI application showing Moscow time on the root page."""

from datetime import datetime
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pytz


with open("templates/index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

app = FastAPI()
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Display current time in Moscow."""
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    html_content = html_template.replace("{{moscow_time}}", moscow_time)
    return HTMLResponse(content=html_content, status_code=200)
