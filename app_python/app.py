from datetime import datetime

import pytz
from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'endpoint']
)

VISITS_FILE = "visits/visits.txt"


def get_visits():
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def update_visits():
    visits = get_visits() + 1
    with open(VISITS_FILE, "w") as f:
        f.write(str(visits))
    return visits


@app.route("/")
def current_time():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    visits = update_visits()
    return f"<h1>Current time in Moscow: {current_time}</h1><p>Visits: {visits}</p>"


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route("/visits")
def visits():
    visits = get_visits()
    return f"<h1>Total visits: {visits}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
