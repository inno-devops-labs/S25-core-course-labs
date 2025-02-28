"""Module with FastAPI application showing Moscow time on the root page."""

from datetime import datetime
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

VISITS_FILE = "/data/visits.txt"

def visit():
    with open(VISITS_FILE, "r") as file:
        v = int(file.read())
    with open(VISITS_FILE, "w") as file:
        file.write(str(v + 1))

with open("templates/index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

app = FastAPI()
Instrumentator().instrument(app).expose(app)
if not os.path.isfile(VISITS_FILE):
    with open(VISITS_FILE, "w") as file:
        file.write("0")

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/visits", response_class=JSONResponse)
async def get_visits():
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
