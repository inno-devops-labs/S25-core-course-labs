import datetime
from flask import render_template, request
from app import app
from app.logging_config import setup_logging

logger = setup_logging()

@app.route('/')
def current_time():
    log_request()

    moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(moscow_timezone)

    return render_template('index.html', current_time=moscow_time)

def log_request():
    logger.info(f"Received request: {request.method} {request.url}")
