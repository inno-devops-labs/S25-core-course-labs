"""
Main application file. Contains the route information and necessary setups.
"""
import os

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

from app_python.app_service import get_time

REQUEST_COUNT = Counter(
    "http_requests_total", "Total number of HTTP requests", ["method", "endpoint"]
)


app = FastAPI()

visits_dir = './data'
visits_file = os.path.join(visits_dir, 'visits')
os.makedirs(visits_dir, exist_ok=True)

def get_visits():
    try:
        with open(visits_file, 'r') as f:
            count = int(f.read())
    except (FileNotFoundError, ValueError):
        count = 0
    return count


def increment_visits():
    count = get_visits() + 1
    with open(visits_file, 'w') as f:
        f.write(str(count))
    return count

@app.get("/", response_class=HTMLResponse)
def show_time(request: Request):
    """
    Shows the current time in Moscow.
    """
    increment_visits()
    REQUEST_COUNT.labels(
        method=request.method, endpoint=request.url.path
    ).inc()  # Increment the counter

    return get_time(request)


@app.get("/metrics")
def metrics():
    """Returns Prometheus metrics in the expected format."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get('/visits')
def visits():
    count = get_visits()
    return f"Total visits: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
