from flask import Flask, render_template
from datetime import datetime
import pytz
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY, start_http_server
import time

app = Flask(__name__)

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
        return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    # Start up the server to expose metrics.
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

