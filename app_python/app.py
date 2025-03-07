from datetime import datetime
import pytz
from flask import Flask, render_template
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Gauge
import os

app = Flask(__name__)

# Define Prometheus metrics
REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")
CURRENT_TIME = Gauge("app_current_time", "Current Moscow time in seconds")

VISITS_FILE = "./data/visits.txt"

if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")


@app.route("/")
def getCurrentTime():
    REQUEST_COUNT.inc()

    moscowTimeZone = pytz.timezone("Europe/Moscow")
    currentTime = datetime.now(moscowTimeZone).strftime("%H:%M:%S")

    CURRENT_TIME.set(datetime.now(moscowTimeZone).timestamp())

    with open(VISITS_FILE, "r+") as f:
        count = int(f.read().strip()) + 1
        f.seek(0)
        f.write(str(count))
        f.truncate()

    return render_template("index.html", time=currentTime)


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


@app.route("/visits")
def visits():
    with open(VISITS_FILE, "r") as f:
        count = f.read().strip()
    return f"Total visits: {count}", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
