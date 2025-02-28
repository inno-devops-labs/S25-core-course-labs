"""Module with FastAPI application showing Moscow time on the root page."""

from datetime import datetime
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

VISITS_FILE = "/data/visits.txt"
with_visits = True


def disable_visits():
    """Disables visits functionality"""
    global with_visits
    with_visits = False


with open("templates/index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

app = FastAPI()
Instrumentator().instrument(app).expose(app)

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


def visit():
    """Increments visits count of root handler"""
    if not with_visits:
        return
    if not os.path.isfile(VISITS_FILE):
        with open(VISITS_FILE, "w") as file:
            file.write("0")
    with open(VISITS_FILE, "r") as file:
        v = int(file.read())
    with open(VISITS_FILE, "w") as file:
        file.write(str(v + 1))


@app.get("/visits", response_class=JSONResponse)
async def get_visits():
    if not with_visits:
        return JSONResponse(content={"visits": 0})
    with open(VISITS_FILE, "r") as file:
        return JSONResponse(content={"visits": int(file.read())})


@app.get("/", response_class=HTMLResponse)
async def read_root():
    visit()
    """Display current time in Moscow."""
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    html_content = html_template.replace("{{moscow_time}}", moscow_time)
    return HTMLResponse(content=html_content, status_code=200)
