from flask import Flask, render_template, Response, jsonify
from prometheus_client import generate_latest, Counter, Histogram
import os

from services.get_time_service import GetTimeService

from config import config

app = Flask(__name__)
app.config.from_mapping(config)

# Prometheus metrics
REQUESTS = Counter(
    'moscow_time_requests_total',
    'Total requests to the Moscow time app'
    )
REQUEST_TIME = Histogram(
    'moscow_time_request_duration_seconds',
    'Time spent processing request')


def get_visit_count():
    """
    Read the current visit count from the visits file.
    Create the file with a count of 0 if it doesn't exist.
    """
    try:
        visits_file = app.config["VISITS_FILE"]
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(visits_file), exist_ok=True)
        
        # If file doesn't exist, create it with count 0
        if not os.path.exists(visits_file):
            with open(visits_file, 'w') as f:
                f.write('0')
            return 0
            
        # Read current count from file
        with open(visits_file, 'r') as f:
            return int(f.read().strip() or '0')
    except Exception as e:
        app.logger.error(f"Error reading visit count: {e}")
        return 0


def increment_visit_count():
    """
    Increment the visit count and save it to the visits file.
    """
    try:
        visits_file = app.config["VISITS_FILE"]
        count = get_visit_count() + 1
        with open(visits_file, 'w') as f:
            f.write(str(count))
        return count
    except Exception as e:
        app.logger.error(f"Error incrementing visit count: {e}")
        return 0


@app.get("/")
@REQUEST_TIME.time()
def get_time():
    """
    Shows the time in the timezone specified in the configuration file.
    """
    REQUESTS.inc()
    # Increment visit counter
    increment_visit_count()
    
    try:
        # Fetch the current time using the service
        current_time = GetTimeService.get_time_by_timezone(
            app.config["TIMEZONE_NAME"]
            )
        # Render the template with the fetched time
        return render_template("current_time.html", current_time=current_time)
    except ValueError as e:
        # Handle invalid timezone errors gracefully
        return f"Error: {e}", 400


@app.get('/visits')
def visits():
    """
    Shows the number of visits to the application in JSON format.
    """
    count = get_visit_count()
    return jsonify({"visits": count})


@app.get('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
