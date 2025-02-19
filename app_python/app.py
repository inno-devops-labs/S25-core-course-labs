from datetime import datetime
import pytz
from flask import Flask, render_template
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Gauge

app = Flask(__name__)

# Define Prometheus metrics
REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")
CURRENT_TIME = Gauge("app_current_time", "Current Moscow time in seconds")


@app.route("/")
def getCurrentTime():
    REQUEST_COUNT.inc()  # Increment request count

    moscowTimeZone = pytz.timezone("Europe/Moscow")
    currentTime = datetime.now(moscowTimeZone).strftime("%H:%M:%S")

    # Store time in seconds since epoch for Prometheus
    CURRENT_TIME.set(datetime.now(moscowTimeZone).timestamp())

    return render_template("index.html", time=currentTime)


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
