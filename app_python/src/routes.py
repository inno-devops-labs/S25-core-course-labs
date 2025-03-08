import time
from datetime import datetime

import prometheus_client
import pytz
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.routing import APIRoute
from fastapi.templating import Jinja2Templates
from prometheus_client import Counter, Histogram

from .config import settings


class MetricsRoute(APIRoute):
    def get_route_handler(self):
        original_handler = super().get_route_handler()

        async def custom_route_handler(request: Request):
            start_time = time.time()
            response = await original_handler(request)
            process_time = time.time() - start_time
            REQUEST_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
                http_status=response.status_code,
            ).inc()
            REQUEST_LATENCY.labels(endpoint=request.url.path).observe(process_time)
            return response

        return custom_route_handler


REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP Requests", ["method", "endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds", "HTTP request latency", ["endpoint"]
)

router = APIRouter(route_class=MetricsRoute)
templates = Jinja2Templates(directory="src/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    curr_time = datetime.now(pytz.timezone(settings.TIMEZONE))
    formatted_time = curr_time.strftime(settings.DATETIME_FORMAT)

    try:
        with open(settings.VISITS_FILE_PATH, "r") as fp:
            count = int(fp.read().strip())
    except FileNotFoundError:
        count = 0
    count += 1
    with open(settings.VISITS_FILE_PATH, "w") as fp:
        fp.write(str(count))

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "timezone": settings.TIMEZONE,
            "formatted_time": formatted_time,
        },
    )


@router.get("/metrics", response_class=Response)
async def metrics():
    return Response(
        content=prometheus_client.generate_latest(), media_type="text/plain"
    )


@router.get("/visits")
async def visits():
    with open(settings.VISITS_FILE_PATH, "r") as fp:
        return {"visits": int(fp.read().strip())}
