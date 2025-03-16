import datetime
from flask import render_template, request
from app import app
from app.logging_config import setup_logging
from app.metrics import before_request, after_request, metrics

logger = setup_logging()

# Register metrics middleware
app.before_request(before_request)
app.after_request(after_request)

# Add metrics endpoint


@app.route('/metrics')
def metrics_endpoint():
    return metrics()


@app.route('/')
def current_time():
    log_request()

    moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(moscow_timezone)

    return render_template('index.html', current_time=moscow_time)


def log_request():
    logger.info(f"Received request: {request.method} {request.url}")
