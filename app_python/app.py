import pytz
from flask import Flask, Response
from datetime import datetime
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

# Global variable with timezone
TIME_ZONE = ""
CONFIG_FILE = "config.txt"

# Prometheus metrics
REQUEST_COUNT = Counter('app_request_count', 'Total number of requests')
REQUEST_TIME = Gauge('app_request_time_seconds', 'Time spent processing requests')
ERROR_COUNT = Counter('app_error_count', 'Total number of errors')


def get_timezone(file=CONFIG_FILE) -> pytz.timezone:
    """
    Loading timezone from configuration file
    """
    try:
        with open(file, "r") as config_file:
            time_zone = config_file.read().strip()

        return pytz.timezone(time_zone)
    except Exception:
        # Default value
        ERROR_COUNT.inc()  # Increment error counter
        return pytz.timezone("Europe/Moscow")


@app.route("/")
def current_time() -> str:
    """
    Returns the current time in timezone formatted as HH:MM:SS.
    """
    global TIME_ZONE

    # Start tracking request time
    start_time = datetime.now()

    # Set up TIME_ZONE if it was not
    if TIME_ZONE == "":
        TIME_ZONE = get_timezone()

    time = datetime.now(TIME_ZONE)
    REQUEST_COUNT.inc()  # Increment request counter
    REQUEST_TIME.set((datetime.now() - start_time).total_seconds())  # Set request time

    return f"Current time in {TIME_ZONE} is {time.strftime('%H:%M:%S')}"


@app.route("/metrics")
def metrics() -> Response:
    """
    Expose Prometheus metrics.
    """
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)