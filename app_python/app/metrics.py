from prometheus_client import (
    Counter, Histogram, Gauge,
    generate_latest, CONTENT_TYPE_LATEST
)
from flask import request, Response
import time

REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)

ACTIVE_REQUESTS = Gauge(
    'app_active_requests',
    'Number of active requests'
)


def before_request():
    request.start_time = time.time()
    ACTIVE_REQUESTS.inc()


def after_request(response):
    request_latency = time.time() - request.start_time
    REQUEST_LATENCY.labels(request.method, request.path
                           ).observe(request_latency)
    REQUEST_COUNT.labels(request.method, request.path,
                         response.status_code).inc()
    ACTIVE_REQUESTS.dec()
    return response


def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
