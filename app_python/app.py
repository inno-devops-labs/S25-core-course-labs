"""
Main application file. Contains the route information and necessary setups.
"""

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

from app_python.app_service import get_time

REQUEST_COUNT = Counter(
    "http_requests_total", "Total number of HTTP requests", ["method", "endpoint"]
)


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def show_time(request: Request):
    """
    Shows the current time in Moscow.
    """
    REQUEST_COUNT.labels(
        method=request.method, endpoint=request.url.path
    ).inc()  # Increment the counter

    return get_time(request)


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
