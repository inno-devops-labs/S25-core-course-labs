from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, PlainTextResponse
from datetime import datetime
import pytz
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
logging.basicConfig(level=logging.INFO)

moscow_time_requests = Counter("moscow_time_requests_total", "Number of times Moscow time was fetched")

DATA_FOLDER = "data"
VISITS_FILE = os.path.join(DATA_FOLDER, "visits.txt")

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def load_visits():
    """Loads the number of visits from the file, defaulting to 0 if the file does not exist."""
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, "r") as f:
        return int(f.read().strip() or 0)

def save_visits(count):
    """Saves the updated visit count to the file."""
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))

visit_count = load_visits()

@app.get("/", response_class=HTMLResponse)
async def get_moscow_time(request: Request):
    """Displays the current Moscow time and updates the visit count."""
    global visit_count
    visit_count += 1
    save_visits(visit_count)
    moscow_time_requests.inc()
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Moscow time fetched: {current_time}")
    return templates.TemplateResponse(request, "index.html", {"time": current_time})

@app.get("/visits", response_class=PlainTextResponse)
async def get_visits():
    """Returns the number of times the root endpoint has been accessed."""
    return PlainTextResponse(str(visit_count))

@app.get("/metrics", response_class=PlainTextResponse)
async def get_metrics():
    """Expose Prometheus metrics."""
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
