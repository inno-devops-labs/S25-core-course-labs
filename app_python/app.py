from flask import Flask, render_template, Response
from prometheus_client import generate_latest, Counter, Histogram

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


@app.get("/")
@REQUEST_TIME.time()
def get_time():
    """
    Shows the time in the timezone specified in the configuration file.
    """
    REQUESTS.inc()
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


@app.get('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
