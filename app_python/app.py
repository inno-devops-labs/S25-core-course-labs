from flask import Flask, render_template
from datetime import datetime
import pytz
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY, start_http_server
import time
import os

app = Flask(__name__)

# Define path for visits file
VISITS_FILE = '/data/visits.txt'

# Ensure the data directory exists
os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)

def get_visit_count():
    """Get the current visit count from file"""
    try:
        if not os.path.exists(VISITS_FILE):
            # Create file with initial count if it doesn't exist
            with open(VISITS_FILE, 'w') as f:
                f.write('0')
            return 0
            
        with open(VISITS_FILE, 'r') as f:
            content = f.read().strip()
            return int(content) if content else 0
    except (IOError, ValueError) as e:
        print(f"Error reading visit count: {e}")
        return 0

def increment_visit_count():
    """Increment and save the visit count"""
    try:
        count = get_visit_count() + 1
        with open(VISITS_FILE, 'w') as f:
            f.write(str(count))
        return count
    except IOError as e:
        print(f"Error saving visit count: {e}")
        return 0

# Define Prometheus metrics
MOSCOW_TIME_REQUESTS = Counter(
    'moscow_time_requests_total',
    'Total number of requests to the Moscow Time app'
)

MOSCOW_TIME_FETCH_LATENCY = Histogram(
    'moscow_time_fetch_seconds',
    'Time spent processing Moscow time request',
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)

@app.route('/metrics')
def metrics():
    """Expose metrics for Prometheus"""
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain'}

@app.route('/')
def index():
    """Serve the index page with the current Moscow time."""
    MOSCOW_TIME_REQUESTS.inc()  # Increment request counter
    
    with MOSCOW_TIME_FETCH_LATENCY.time():  # Measure request duration
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
        visit_count = increment_visit_count()
        return render_template('index.html', current_time=current_time, visits=visit_count)

@app.route('/visits')
def visits():
    """Display the total number of visits"""
    visit_count = get_visit_count()
    return {'total_visits': visit_count}

if __name__ == '__main__':
    # Start up the server to expose metrics.
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

