from datetime import datetime
import logging
import os
import sys
import pytz
from flask import Flask, render_template, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# Setup logging
log_dir = '/home/appuser/logs'
# Create log directory if it doesn't exist (for local development)
os.makedirs(log_dir, exist_ok=True)

# Create visits directory if it doesn't exist
visits_dir = '/home/appuser/data'
os.makedirs(visits_dir, exist_ok=True)
visits_file = f'{visits_dir}/visits'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(f'{log_dir}/app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Define Prometheus metrics
PAGE_VIEWS = Counter('page_views_total', 'Number of page views', ['page'])
HEALTH_CHECKS = Counter('health_checks_total', 'Number of health checks')
HTTP_REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration in seconds', ['endpoint'])

def get_visit_count():
    """Get the current visit count from the file."""
    try:
        if os.path.exists(visits_file):
            with open(visits_file, 'r') as f:
                return int(f.read().strip())
        return 0
    except Exception as e:
        logger.error("Error reading visit count: %s", e)
        return 0

def increment_visit_count():
    """Increment the visit count in the file."""
    try:
        count = get_visit_count() + 1
        with open(visits_file, 'w') as f:
            f.write(str(count))
        return count
    except Exception as e:
        logger.error("Error incrementing visit count: %s", e)
        return -1

@app.route("/")
def index():
    """Display current Moscow time."""
    logger.info("Index page accessed by %s", request.remote_addr)
    PAGE_VIEWS.labels(page='index').inc()
    visit_count = increment_visit_count()
    logger.info("Visit count incremented to %s", visit_count)
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz)
    return render_template("index.html", current_time=moscow_time)

@app.route("/visits")
def visits():
    """Display the visit count."""
    logger.info("Visits page accessed by %s", request.remote_addr)
    PAGE_VIEWS.labels(page='visits').inc()
    visit_count = get_visit_count()
    return render_template("visits.html", visit_count=visit_count)

@app.route("/health")
def health():
    """Health check endpoint."""
    logger.info("Health check performed")
    HEALTH_CHECKS.inc()
    return {"status": "healthy"}, 200


@app.route('/metrics')
def metrics():
    """Expose Prometheus metrics."""
    logger.info("Metrics endpoint accessed")
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    logger.error("404 error: %s - %s", request.path, e)
    PAGE_VIEWS.labels(page='404').inc()
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    logger.error("500 error: %s", e)
    return render_template("500.html"), 500


if __name__ == "__main__":
    logger.info("Application starting")
    app.run(debug=True, host="0.0.0.0")