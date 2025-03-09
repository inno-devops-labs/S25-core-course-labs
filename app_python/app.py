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

VISITS_DIR = './data'
VISITS_FILE = os.path.join(VISITS_DIR, 'visits')
os.makedirs(VISITS_DIR, exist_ok=True)

def get_visits():
    """
    Retrieves the current visit count from the file.
    Returns 0 if the file doesn't exist or contains invalid data.
    """
    try:
        with open(VISITS_FILE, 'r', encoding='utf-8') as f:
            count = int(f.read())
    except (FileNotFoundError, ValueError):
        count = 0
    return count

def increment_visits():
    """
    Increments the visit count and writes it to the visits file.
    Returns the updated visit count.
    """
    count = get_visits() + 1
    with open(VISITS_FILE, 'w', encoding='utf-8') as f:
        f.write(str(count))
    return count

@app.get("/", response_class=HTMLResponse)
def show_time(request: Request):
    """
    Shows the current time in Moscow.
    Increments the visit count on each request.
    """
    increment_visits()
    REQUEST_COUNT.labels(
        method=request.method, endpoint=request.url.path
    ).inc()  # Increment the counter

    return get_time(request)

@app.get("/metrics")
def metrics():
    """
    Returns Prometheus metrics in the expected format.
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get('/visits')
def visits():
    """
    Returns the total number of visits.
    """
    count = get_visits()
    return f"Total visits: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
