from flask import Flask
from datetime import datetime
import pytz
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Create Prometheus metrics
REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['endpoint', 'http_status']
)

def get_msk_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))

@app.route('/')
def show_time():
    msk_time = get_msk_time()
    REQUEST_COUNT.labels(endpoint='/', http_status='200').inc()
    return f"<h1>Current Time in Moscow: {msk_time.strftime('%H:%M:%S')}</h1>"

# Create separate metrics app on port 8000
metrics_app = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5000, metrics_app)
