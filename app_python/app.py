from flask import Flask, render_template, Response, request
from datetime import datetime
import pytz
import time
from prometheus_client import (Counter, Histogram,
                               generate_latest, CONTENT_TYPE_LATEST)

# Initialize the Flask application
app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"]
)


def get_moscow_time():
    """
        Get the current time in Moscow.
    """
    return datetime.now(pytz.timezone('Europe/Moscow'))


def format_time(time):
    """
        Format into a string in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def show_time():
    """
        Route handler for the root URL.
    """
    start_time = time.time()
    moscow_time = get_moscow_time()
    formatted_moscow_time = format_time(moscow_time)

    response = render_template(
        'index.html',
        formatted_moscow_time=formatted_moscow_time
    )

    # Update Prometheus metrics
    process_time = time.time() - start_time
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        http_status=200
    ).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).observe(process_time)

    return response


@app.route('/metrics')
def metrics():
    """
        Expose Prometheus metrics.
    """
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
