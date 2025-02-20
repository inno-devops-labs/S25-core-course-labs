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


registry = CollectorRegistry()
current_time_gauge = Gauge(
    'current_moscow_time',
    'Current time in Moscow as a Unix timestamp',
    registry=registry
)


@app.route('/')
def show_moscow_time():
    # Get the current time in Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    # Update the gauge with the current timestamp (in seconds)
    current_time_gauge.set(current_time.timestamp())
    return (
        f"<h1>Welcome to my Python Web App!</h1>"
        f"<h1>Current Time in Moscow: {current_time_str} MSK</h1>"
    )


@app.route('/metrics')
def metrics():
    # Expose metrics to Prometheus
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
