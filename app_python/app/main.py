from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse
from datetime import datetime
import pytz
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
logging.basicConfig(level=logging.INFO)

moscow_time_requests = Counter(
    "moscow_time_requests_total", "Number of times Moscow time was fetched"
)


@app.get("/", response_class=HTMLResponse)
async def get_moscow_time(request: Request):
    """Displays the current Moscow time"""
    moscow_time_requests.inc()
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Moscow time fetched: {current_time}")

    return templates.TemplateResponse(request, "index.html", {"time": current_time})


@app.get("/metrics", response_class=PlainTextResponse)
async def get_metrics():
    """Expose Prometheus metrics"""
    return PlainTextResponse(
        generate_latest(), media_type=CONTENT_TYPE_LATEST
    )
