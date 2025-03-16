import datetime
import os
from flask import render_template, request
from app import app
from app.logging_config import setup_logging
from app.metrics import before_request, after_request, metrics

logger = setup_logging()

# Register metrics middleware
app.before_request(before_request)
app.after_request(after_request)

# Path to the visits file
VISITS_FILE = '/data/visits'

# Function to read the visit count
def read_visit_count():
    try:
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'r') as f:
                return int(f.read().strip() or '0')
        return 0
    except Exception as e:
        logger.error(f"Error reading visit count: {e}")
        return 0

# Function to update the visit count
def update_visit_count():
    try:
        count = read_visit_count() + 1
        os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
        with open(VISITS_FILE, 'w') as f:
            f.write(str(count))
        return count
    except Exception as e:
        logger.error(f"Error updating visit count: {e}")
        return 0

# Add metrics endpoint
@app.route('/metrics')
def metrics_endpoint():
    return metrics()

# Add visits endpoint
@app.route('/visits')
def visits():
    count = read_visit_count()
    return render_template('visits.html', count=count)

@app.route('/')
def current_time():
    log_request()
    # Update visit count
    visit_count = update_visit_count()
    logger.info(f"Visit count: {visit_count}")

    moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(moscow_timezone)

    return render_template(
        'index.html', current_time=moscow_time, visit_count=visit_count
    )

def log_request():
    logger.info(f"Received request: {request.method} {request.url}")
