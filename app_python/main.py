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

app = FastAPI()
templates = Jinja2Templates(directory="templates")

logger = logging.getLogger("my_app")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s '
                              '- %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@app.middleware("http")
async def update_metrics(request: Request, call_next):
    response = await call_next(request)
    get_metrics(request, response)
    return response


# Log request information
@app.middleware("http")
async def log_request_info(request: Request, call_next):
    logger.info(f"Received request: {request.method} "
                f"{request.url} from {request.client.host}")
    response = await call_next(request)
    return response


@app.get("/", response_class=HTMLResponse)
async def read_time(request: Request):
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse(
        request,
        "index.html",
        {"time": formatted_time}
    )


@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/health")
async def health():
    return "OK", 200
