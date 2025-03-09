from flask import Flask, request
from datetime import datetime
import pytz
import logging
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)

metrics = PrometheusMetrics(app,
                            export_defaults=True,
                            group_by='endpoint',
                            defaults_prefix='flask',
                            path='/metrics')

# Configure logging to output to stdout
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Create a logger instance
logger = logging.getLogger(__name__)

# Configure visits file
visits_dir = './data'
visits_file = os.path.join(visits_dir, 'visits')

# Ensure the data directory exists
os.makedirs(visits_dir, exist_ok=True)


def get_visits():
    try:
        with open(visits_file, 'r') as f:
            count = int(f.read())
    except (FileNotFoundError, ValueError):
        count = 0
    return count


def increment_visits():
    count = get_visits() + 1
    with open(visits_file, 'w') as f:
        f.write(str(count))
    return count


# Route for the root URL where moscow_time function will be executed
@app.route('/')
def moscow_time():
    increment_visits()

    # Setting up a timezone
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Formatting the date and time
    moscow_time = datetime.now(moscow_tz).strftime('%d-%m-%Y    %H:%M:%S')

    # Log the request details
    logger.info(f"Request received from {request.remote_addr}" +
                f" at {moscow_time}")

    # Returning the date and time to the web page
    return f"Current time in Moscow: {moscow_time}"


@app.route('/visits')
def visits():
    count = get_visits()
    return f"Total visits: {count}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
