import os
from datetime import datetime

import pytz
from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

VISITS_FILE = "data/visits.txt"

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "Total number of HTTP requests")


@app.route('/')
def display_time():
    REQUEST_COUNT.inc()
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    visits_cnt = get_visits() + 1
    save_visits(visits_cnt)
    return f"<h1>Current Time in Moscow: {current_time}</h1>"


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/visits')
def visits():
    visits_cnt = get_visits()
    return f"<h1>Number of Visits: {visits_cnt}</h1>"


def get_visits():
    try:
        with open(VISITS_FILE, "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_visits(count):
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
    with open(VISITS_FILE, "w") as file:
        file.write(str(count))


if __name__ == "__main__":
    app.run(debug=True)
