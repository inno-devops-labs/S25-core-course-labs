import time
from datetime import datetime

import prometheus_client
import pytz
from flask import Flask, render_template, request, Response
from prometheus_client import Counter, Histogram, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total", "Total number of HTTP requests",
    ["method", "endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency", ["endpoint"]
)


@app.route("/")
def index():
    start_time = time.time()
    moscow_time_zone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_time_zone).strftime("%Y-%m-%d %H:%M:%S")
    rendering = render_template("index.html", time=moscow_time)

    finish_time = time.time() - start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path,
                         http_status=200).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).observe(finish_time)
    return rendering


@app.route("/metrics")
def metrics():
    return Response(prometheus_client.generate_latest(),
                    mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
