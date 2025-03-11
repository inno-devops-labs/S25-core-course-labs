from datetime import datetime
import pytz
import os
from flask import Flask, render_template
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Gauge

app = Flask(__name__)

# Counter for tracking requests
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

# Gauge for tracking the last time the /metrics endpoint was accessed
LAST_METRICS_ACCESS = Gauge('app_last_metrics_access_time', 'Last time the /metrics endpoint was accessed')

# File to store the number of visits
VISITS_FILE = 'visits.txt'


def increment_visits():
    """Increment the visit count and save it to the file."""
    try:
        with open(VISITS_FILE, 'r') as f:
            visits = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        visits = 0

    visits += 1

    with open(VISITS_FILE, 'w') as f:
        f.write(str(visits))

    return visits


def get_visits():
    """Get the current visit count from the file."""
    try:
        with open(VISITS_FILE, 'r') as f:
            visits = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        visits = 0

    return visits


@app.route("/")
def hello_world():
    # Increment the request counter
    REQUEST_COUNT.inc()

    # Increment the visit count
    increment_visits()

    # Getting Moscow time
    msk_time = get_moscow_time()
    return render_template('home_page.html', time=msk_time)


@app.route("/metrics")
def metrics():
    # Update the last access time gauge
    LAST_METRICS_ACCESS.set_to_current_time()

    # Return the metrics in the format Prometheus expects
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route("/visits")
def show_visits():
    # Get the current visit count
    visits = get_visits()
    return render_template('visits.html', visits=visits)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


def get_moscow_time():
    return datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d-%m-%Y %H:%M:%S')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)