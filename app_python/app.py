from datetime import datetime
import pytz
import os
from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)

# Define a counter metric for tracking requests
REQUEST_COUNT = Counter('python_app_requests_total', 'Total number of requests')

# ✅ Use /data for persistence
VISITS_DIR = "/data"
VISITS_FILE = os.path.join(VISITS_DIR, "visits.txt")

# ✅ Ensure the /data directory exists
os.makedirs(VISITS_DIR, exist_ok=True)

# ✅ Ensure visits.txt exists before reading
if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")  # Initialize visits count

def load_visits():
    """Read visit count from file."""
    with open(VISITS_FILE, "r") as f:
        return int(f.read().strip())

def save_visits(count):
    """Write visit count to file."""
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))

@app.route("/")
def show_time():
    REQUEST_COUNT.inc()  # Increment Prometheus counter
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

    # Update visit counter
    visits = load_visits() + 1
    save_visits(visits)

    return f"<h1>Current Time in Moscow: {current_time}</h1><p>Visits: {visits}</p>"

@app.route("/visits")
def visits():
    visits = load_visits()
    return f"<h1>Total Visits: {visits}</h1>"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
