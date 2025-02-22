from datetime import datetime
import pytz
from flask import Flask
from prometheus_client import start_http_server, Counter, Histogram
import time

# Initialize the Flask app
app = Flask(__name__)

# Create metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency')


@app.route('/')
def hello():
    """
    Main endpoint: Hello message with request count and latency tracking.
    """
    REQUEST_COUNT.inc()  # Increment request count
    with REQUEST_LATENCY.time():  # Measure latency
        time.sleep(0.5)
    return "Hello, World!"

@app.route('/moscow_time')
def moscow_time():
    """
    Endpoint to display the current time in Moscow.
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Time in Moscow</h1><p>{current_time}</p>"

# Start the app and expose metrics
if __name__ == '__main__':
    start_http_server(8001)  # Expose metrics on port 8001
    app.run(host='0.0.0.0', port=8000, debug=True)
