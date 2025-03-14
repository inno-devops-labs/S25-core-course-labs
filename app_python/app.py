from flask import Flask, jsonify, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Gauge
from datetime import datetime
import os
import pytz

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')
LAST_METRICS_ACCESS = Gauge('app_last_metrics_access_time', 'Last time the /metrics endpoint was accessed')
VISITS_FILE = "/data/visits.txt"

if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")


@app.route("/")
def moscow_time():
    REQUEST_COUNT.inc()
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    increment_visits()
    return f"<h1>Current time in Moscow city is {current_time}</h1>"


@app.route("/metrics")
def metrics():
    LAST_METRICS_ACCESS.set_to_current_time()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route("/visits")
def visits():
    return jsonify({"visits": read_visits()})


def increment_visits():
    try:
        with open(VISITS_FILE, "r+") as f:
            count = int(f.read().strip() or 0) + 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
    except FileNotFoundError:
        print("visits.txt not found, creating a new one.")
        with open(VISITS_FILE, "w") as f:
            f.write("1")


def read_visits():
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip() or 0)
    except FileNotFoundError:
        return 0


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
