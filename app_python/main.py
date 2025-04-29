import os
import threading
from datetime import datetime
from time import monotonic

import pytz
from flask import Flask, render_template, g, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

TIMEZONE = "Europe/Moscow"
TIME_FORMAT = "%Y.%m.%d %H:%M:%S"
PAGE = "index.html"

COUNTER_FOLDER = "visits"
COUNTER_FILE = "visits.txt"
COUNTER_FILE_PATH = os.path.join(COUNTER_FOLDER, COUNTER_FILE)

app = Flask(__name__)

REQUESTS_COUNT = Counter(
    "http_requests_total", "Total count of HTTP requests", ["method", "path", "http_code"]
)
REQUESTS_LATENCY = Histogram(
    "http_request_duration_seconds", "Duration in seconds of HTTP requests", ["path"]
)


def increment_counter():
    if not os.path.exists(COUNTER_FOLDER):
        os.makedirs(COUNTER_FOLDER)

    if os.path.exists(COUNTER_FILE_PATH):
        with open(COUNTER_FILE_PATH, "r") as f:
            try:
                count = int(f.read()) + 1
            except ValueError:
                count = 1
    else:
        count = 1

    with open(COUNTER_FILE_PATH, "w") as f:
        f.write(str(count))

    return count


lock = threading.Lock()


@app.before_request
def record_start_time():
    """Store start time in Flask's global context"""
    g.start_time = monotonic()
    with lock:
        g.requests_count = increment_counter()


@app.after_request
def track_metrics(response):
    """Update Prometheus metrics after each request"""
    duration = monotonic() - g.start_time
    REQUESTS_LATENCY.labels(
        path=request.path
    ).observe(duration)

    REQUESTS_COUNT.labels(
        method=request.method,
        path=request.path,
        http_code=response.status_code
    ).inc()

    return response


@app.route("/", methods=["GET"])
def index():
    """
    Returns html page that displays time in Moscow
    """
    start = monotonic()
    time = datetime.now(pytz.timezone(TIMEZONE)).strftime(TIME_FORMAT)
    page = render_template(PAGE, time=time)
    finish = monotonic()

    REQUESTS_LATENCY.labels(path="/").observe(finish - start)

    REQUESTS_COUNT.labels(
        method="GET",
        path="/",
        http_code=200,
    ).inc()

    return page


@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route("/visits", methods=["GET"])
async def get_visits():
    return f"Visits: {g.requests_count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
