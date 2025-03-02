from flask import Flask, render_template
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import Counter, Histogram
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'HTTP Request Latency', ['method', 'endpoint'])

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route('/')
def start():
    start_time = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    response = render_template('index.html')
    REQUEST_LATENCY.labels(method='GET', endpoint='/').observe(time.time() - start_time)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)