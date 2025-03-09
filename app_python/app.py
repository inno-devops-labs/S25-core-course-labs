import os

from flask import Flask, jsonify, Response
from datetime import datetime
import pytz
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)

REQUEST_COUNT = Counter("request_count", "Requests Counter", ["method", "endpoint"])


@app.route("/")
def moscow_time():
    increment_visits()
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()

    tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(tz)

    data = {
        "timezone": tz.zone,
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    return jsonify(data)


@app.route("/metrics")
def metrics():
    increment_visits()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route("/visits")
def visits():
    data = {
        "visits": read_visits(),
    }

    return jsonify(data)


def increment_visits():
    file_path = os.getenv("VISITS_FILE_PATH", "data/visits.txt")
    try:
        with open(file_path, "r") as f:
            count = int(f.read().strip() or 0)
    except FileNotFoundError:
        print("visits file not found")
        count = 0

    count += 1

    with open(file_path, "w") as f:
        f.write(str(count))


def read_visits():
    file_path = os.getenv("VISITS_FILE_PATH", "data/visits.txt")
    try:
        with open(file_path, "r") as f:
            count = int(f.read().strip() or 0)
    except FileNotFoundError:
        print("visits files not found")
        count = 0

    return count


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
