from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import pytz
import os
import logging
import sys
from prometheus_client import Counter, Histogram, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Moscow Time</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }
        .container {
            text-align: center;
            padding: 2rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .time {
            font-size: 3rem;
            color: #1a73e8;
            margin: 1rem 0;
        }
        .date {
            font-size: 1.5rem;
            color: #5f6368;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="time">{{ time }}</div>
        <div class="date">{{ date }}</div>
    </div>
</body>
</html>
'''

# Prometheus metrics
REQUEST_COUNT = Counter('app_request_count', 'Total number of requests', ['endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['endpoint'])

@app.before_request
def log_request():
    logger.info(
        f"Received {request.method} request from {request.remote_addr} to {request.path}")


@app.after_request
def log_response(response):
    logger.info(f"Returning response with status {response.status}")
    return response


@app.route('/')
def index():
    REQUEST_COUNT.labels(endpoint='/').inc()
    with REQUEST_LATENCY.labels(endpoint='/').time():
        # Increment visit counter
        increment_visit_counter()
        
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_tz)

        time_str = moscow_time.strftime('%H:%M:%S')
        date_str = moscow_time.strftime('%B %d, %Y')

        logger.info(f"Generated Moscow time: {time_str} and date: {date_str}")
        return render_template_string(HTML_TEMPLATE, time=time_str, date=date_str)


@app.route('/health')
def health():
    REQUEST_COUNT.labels(endpoint='/health').inc()
    with REQUEST_LATENCY.labels(endpoint='/health').time():
        logger.info("Health check endpoint called")
        return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})


@app.route('/visits')
def visits():
    REQUEST_COUNT.labels(endpoint='/visits').inc()
    with REQUEST_LATENCY.labels(endpoint='/visits').time():
        visit_count = get_visit_count()
        logger.info(f"Visits endpoint called, current count: {visit_count}")
        return jsonify({"visits": visit_count})


# Functions for visit counter persistence
def get_visit_count():
    # Use /data directory for persistent storage in StatefulSet
    data_dir = '/data'
    # Fallback to current directory if /data is not available (for local development)
    if not os.path.exists(data_dir):
        data_dir = os.path.dirname(__file__)
    
    visits_file = os.path.join(data_dir, 'visits')
    try:
        if os.path.exists(visits_file):
            with open(visits_file, 'r') as f:
                count = f.read().strip()
                return int(count) if count else 0
        return 0
    except Exception as e:
        logger.error(f"Error reading visit count: {e}")
        return 0


def increment_visit_counter():
    # Use /data directory for persistent storage in StatefulSet
    data_dir = '/data'
    # Fallback to current directory if /data is not available (for local development)
    if not os.path.exists(data_dir):
        data_dir = os.path.dirname(__file__)
        
    visits_file = os.path.join(data_dir, 'visits')
    try:
        count = get_visit_count() + 1
        with open(visits_file, 'w') as f:
            f.write(str(count))
        logger.info(f"Visit counter incremented to {count}")
        return count
    except Exception as e:
        logger.error(f"Error incrementing visit count: {e}")
        return 0


# Add prometheus wsgi middleware
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    logger.info("Starting Moscow Time application")
    app.run(host='0.0.0.0', debug=os.environ.get('FLASK_DEBUG', False))
