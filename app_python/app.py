from flask import Flask, render_template
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import Counter, Histogram
import time
import os

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'HTTP Request Latency', ['method', 'endpoint'])

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

VISITS_FILE = "/data/visits.txt"

@app.route('/')
def start():
    with open(VISITS_FILE, "r+") as f:
        visits = int(f.read())
        visits += 1
        f.seek(0)
        f.write(str(visits))
        f.truncate()
    start_time = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    response = render_template('index.html')
    REQUEST_LATENCY.labels(method='GET', endpoint='/').observe(time.time() - start_time)
    return response

@app.route('/visits')
def visits():
    with open(VISITS_FILE, "r") as f:
        visits = f.read()
    return f"Number of visits: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)