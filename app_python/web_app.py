from datetime import datetime
import pytz
import os
from flask import Flask
from prometheus_client import start_http_server, Counter, Histogram
import time

# Initialize the Flask app
app = Flask(__name__)


# Check if running in a test environment
if "PYTEST_CURRENT_TEST" in os.environ or "GITHUB_ACTIONS" in os.environ:
    VISITS_FILE = "visits_test"
else:
    VISITS_FILE = "/app/visits"

# Ensure the file exists
if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")


# Ensure the file exists and is not a directory
if os.path.isdir(VISITS_FILE):
    os.rmdir(VISITS_FILE)  # Remove if it's mistakenly a directory


# Create metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency')


def get_visit_count():
    """Retrieve visit count from file."""
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip())
    except ValueError:
        return 0  # Default to 0 if file content is invalid


def increment_visit_count():
    """Increment and save visit count to file."""
    count = get_visit_count() + 1
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))
    return count


@app.route('/')
def hello():
    """Main endpoint: Hello message with request count and latency tracking."""
    REQUEST_COUNT.inc()  # Increment request count
    with REQUEST_LATENCY.time():  # Measure latency
        time.sleep(0.5)
    return "Hello, World!"


@app.route('/moscow_time')
def moscow_time():
    """Endpoint to display the current time in Moscow."""
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Time in Moscow</h1><p>{current_time}</p>"


@app.route('/visits')
def visits():
    """Endpoint to return the number of visits."""
    count = increment_visit_count()
    return f"Visit count: {count}"


# Start the app and expose metrics
if __name__ == '__main__':
    start_http_server(8001)
    app.run(host='0.0.0.0', port=8000, debug=False)
