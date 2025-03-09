import pytz
import os
from flask import Flask, Response
from datetime import datetime
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

# Global variable with timezone
TIME_ZONE = ""
CONFIG_FILE = "config.txt"
VISITS_DIRECTORY = "visits"
VISITS_FILE = "visits"
VISITS = 0

# Prometheus metrics
REQUEST_COUNT = Counter('app_request_count', 'Total number of requests')
REQUEST_TIME = Gauge('app_request_time_seconds',
                     'Time spent processing requests')
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
    global VISITS

    VISITS += 1

    with open(os.path.join(VISITS_DIRECTORY, VISITS_FILE), "w") as visits_file:
        visits_file.write(str(VISITS))

    # Start tracking request time
    start_time = datetime.now()

    # Set up TIME_ZONE if it was not
    if TIME_ZONE == "":
        TIME_ZONE = get_timezone()

    time = datetime.now(TIME_ZONE)
    REQUEST_COUNT.inc()  # Increment request counter
    REQUEST_TIME.set((datetime.now() -
                      start_time).total_seconds())  # Set request time

    return f"Current time in {TIME_ZONE} is {time.strftime('%H:%M:%S')}"


@app.route("/metrics")
def metrics() -> Response:
    """
    Expose Prometheus metrics.
    """
    return Response(generate_latest(), mimetype="text/plain")


@app.route("/visits")
def visits():
    # Here visits also counts, since it is also access to the application
    global VISITS
    VISITS += 1

    with open(os.path.join(VISITS_DIRECTORY, VISITS_FILE), "w") as visits_file:
        visits_file.write(str(VISITS))

    return f"Number of visits is: {VISITS}"


if __name__ == "__main__":
    try:
        with open(os.path.join(VISITS_DIRECTORY, VISITS_FILE), "r") as visits_file:
            VISITS = int(visits_file.read())
    except Exception:
        if os.path.exists(os.path.join(VISITS_DIRECTORY, VISITS_FILE)):
            os.remove(os.path.join(VISITS_DIRECTORY, VISITS_FILE))
        elif not os.path.exists(VISITS_DIRECTORY):
            os.makedirs(VISITS_DIRECTORY)

            VISITS = 0

        with open(os.path.join(VISITS_DIRECTORY, VISITS_FILE), "w") as visits_file:
            visits_file.write(str(VISITS))

    app.run(host="0.0.0.0", port=5000, debug=True)
