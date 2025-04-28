from flask import Flask, Response
from datetime import datetime
import pytz
import logging
from pythonjsonlogger import jsonlogger
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST, Summary
import time


app = Flask(__name__)


log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
log_handler.setFormatter(formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


REQUEST_COUNT = Counter('app_request_count', 'Total app HTTP request count', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['method', 'endpoint'])
REQUEST_TIME = Summary('app_request_processing_seconds', 'Time spent processing request')


@app.route("/")
def home():
    start_time = time.time()

    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Current time in Moscow: {current_time}")

    REQUEST_COUNT.labels(method='GET', endpoint='/', http_status=200).inc()
    REQUEST_LATENCY.labels(method='GET', endpoint='/').observe(time.time() - start_time)

    return f"<h1>Current Time in Moscow: {current_time}</h1>"


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@REQUEST_TIME.time()
def process_request():
    time.sleep(0.001)
    return "done"


@app.route('/test')
def test():
    process_request()
    REQUEST_COUNT.labels(method='GET', endpoint='/test', http_status=200).inc()
    return "Test endpoint"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)