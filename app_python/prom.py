from fastapi import Request
from prometheus_client import Counter, Histogram
import time
from starlette.responses import Response

REQUEST_COUNT = Counter(
    'request_count', 'App Request Count',
    ['app_name', 'method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'request_latency_seconds', 'Request latency',
    ['app_name', 'endpoint']
)


def get_metrics(request: Request, response: Response):
    start_time = time.time()

    resp_time = time.time() - start_time
    REQUEST_LATENCY.labels('test_app', request.url.path).observe(resp_time)

    REQUEST_COUNT.labels('test_app', request.method, request.url.path,
                         response.status_code).inc()

    return response
