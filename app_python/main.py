import os
from flask import Flask, Response
from datetime import datetime
import pytz
from prometheus_client import (
    CollectorRegistry,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST
)

app = Flask(__name__)

# Prometheus registry and gauge metric setup
registry = CollectorRegistry()
current_time_gauge = Gauge(
    'current_moscow_time',
    'Current time in Moscow as a Unix timestamp',
    registry=registry
)

# File path for persisting the visit counter
VISITS_FILE = 'visits'


def get_visits():
    """Read the current visit count from the persistent file."""
    if os.path.exists(VISITS_FILE):
        try:
            with open(VISITS_FILE, 'r') as f:
                return int(f.read().strip())
        except ValueError:
            return 0
    return 0


def update_visits():
    """Increment the visit count and save it to the file."""
    count = get_visits() + 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))
    return count


@app.route('/')
def show_moscow_time():
    # Get the current time in Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    # Update the Prometheus gauge with the current timestamp (in seconds)
    current_time_gauge.set(current_time.timestamp())
    # Update visit counter
    update_visits()
    return (
        f"<h1>Welcome to my Python Web App!</h1>"
        f"<h1>Current Time in Moscow: {current_time_str} MSK</h1>"
    )


@app.route('/visits')
def visits():
    """Return the current number of visits."""
    count = get_visits()
    return f"<h2>Number of visits: {count}</h2>"


@app.route('/metrics')
def metrics():
    # Expose Prometheus metrics
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
