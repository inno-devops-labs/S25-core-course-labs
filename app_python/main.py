import logging
import sys
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from prom import get_metrics
import pytz
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

logger = logging.getLogger("my_app")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s '
                              '- %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

VISIT_FILE_PATH = os.getenv("VISIT_FILE_PATH", "/data/visits")


def load_visits():
    try:
        if not os.path.exists(VISIT_FILE_PATH):
            return 0
        with open(VISIT_FILE_PATH, "r") as f:
            return int(f.read().strip())
    except Exception as e:
        print(f"Visit load error: {e}")
        return 0


def save_visits(count: int):
    try:
        os.makedirs(os.path.dirname(VISIT_FILE_PATH), exist_ok=True)
        with open(VISIT_FILE_PATH, "w") as f:
            f.write(str(count))
    except Exception as e:
        print(f"Visit save error: {e}")


@app.middleware("http")
async def update_metrics(request: Request, call_next):
    response = await call_next(request)
    get_metrics(request, response)
    return response


@app.middleware("http")
async def log_request_info(request: Request, call_next):
    logger.info(f"Received request: {request.method} "
                f"{request.url} from {request.client.host}")
    response = await call_next(request)
    return response


@app.get("/", response_class=HTMLResponse)
async def read_time(request: Request):
    save_visits(load_visits() + 1)
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse(
        request,
        "index.html",
        {"time": formatted_time}
    )


@app.get("/visits")
async def get_visits():
    visit_count = load_visits()
    return {"visit_count": visit_count}


@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/health")
async def health():
    return "OK", 200
