from datetime import datetime
import pytz
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, Response
import logging_loki
from prometheus_client import Counter, generate_latest, Summary

app = Flask(__name__)
REQUEST_COUNT = Counter('request_count', 'Total HTTP requests')
REQUEST_LATENCY = Summary('request_latency_seconds', 'Latency of requests in seconds')

def get_moscow_time():
    """
    Get the current time in Moscow timezone.
    Returns:
        str: The current time in Moscow formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    try:
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
        return moscow_time
    except Exception as e:
        app.logger.error(f"Error fetching Moscow time: {e}")
        return "Error fetching Moscow time"

@app.before_request
def before_request():
    REQUEST_COUNT.inc()

@app.route('/')
def home():
    with REQUEST_LATENCY.time():
        moscow_time = get_moscow_time()
    return f"<h1>Current time in Moscow: {moscow_time}</h1>"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

@app.route('/health')
def health():
    return "OK", 200

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    Args:
        error (Exception): The error object.
    Returns:
        str: Error message with HTTP 404 status code.
    """
    app.logger.warning(f"404 error encountered: {error}")
    return "<h1>404 - Page Not Found</h1><p>The requested URL was not found on the server.</p>", 404

if __name__ == '__main__':
    handler = logging_loki.LokiHandler(
        url="http://loki:3100/loki/api/v1/push",
        tags={"application": "app_python"},
        version="1",
    )
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    app.run(host='0.0.0.0', port=5001, debug=False)
