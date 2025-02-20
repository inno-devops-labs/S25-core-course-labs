from datetime import datetime, time
from time import monotonic
from typing import Callable

import pytz
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.routing import APIRoute
from prometheus_client import Counter, Histogram, generate_latest as generate_latest_prometheus_metrics
from pydantic import BaseModel

# Host and port to run the application
APP_HOST = "0.0.0.0"
APP_PORT = 8001

# Time format to display the time and an example of the time in this format
TIME_FORMAT = "%H:%M:%S"
TIME_FORMAT_EXAMPLE = "23:45:01"

# Timezone to display the time
TIMEZONE = "Europe/Moscow"

# HTML file with the web page
HTML_FILENAME = "index.html"

REQUESTS_COUNT = Counter(
    "http_requests_total", "Total count of HTTP requests", ["method", "path", "http_code"]
)
REQUESTS_LATENCY = Histogram(
    "http_request_duration_seconds", "Duration in seconds of HTTP requests", ["path"]
)


class MetricsAPIRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_handler = super().get_route_handler()

        async def custom_route_handler(request: Request):
            start_time = monotonic()
            response = await original_handler(request)
            finish_time = monotonic()

            process_time = finish_time - start_time

            REQUESTS_COUNT.labels(
                method=request.method,
                path=request.url.path,
                http_code=response.status_code,
            ).inc()

            REQUESTS_LATENCY.labels(path=request.url.path).observe(process_time)

            return response

        return custom_route_handler


# Create a FastAPI application
app = FastAPI()
app.router.route_class = MetricsAPIRoute


class TimeResponse(BaseModel):
    """
    Response model with a time field
    """

    time: time

    model_config = {
        # Custom JSON encoder for time objects to serialize
        # them as strings in the specified format
        "json_encoders": {time: lambda v: v.strftime(TIME_FORMAT)},
        # Custom JSON schema with an example
        "json_schema_extra": {"example": {"time": TIME_FORMAT_EXAMPLE}},
    }


@app.get("/", response_class=HTMLResponse)
def get_current_time_html():
    """
    Returns the HTML web page that displays the current time
    in the specified timezone using API
    """
    return HTMLResponse(open(HTML_FILENAME).read())


@app.get("/api/time", response_model=TimeResponse)
def get_current_time():
    """
    Returns the current time in the specified timezone
    """
    return TimeResponse(time=datetime.now(pytz.timezone(TIMEZONE)).time())


@app.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    return PlainTextResponse(generate_latest_prometheus_metrics())


if __name__ == "__main__":
    # Run the application using Uvicorn
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
