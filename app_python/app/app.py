"""
This is a simple python web application that shows current time in Moscow.
Author: Aleksandr Ryabov (a.ryabov@innoplis.university)
"""

import pytz
import os
from datetime import datetime
from flask import Flask, render_template, Response
from prometheus_client import generate_latest, REGISTRY, Counter, Gauge

# ========== Metrics Setup ==========
REQUEST_COUNTER = Counter(
    "app_http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint", "status"],
)

HEALTH_GAUGE = Gauge(
    "app_health_status", "Application Health Status (1=healthy, 0=unhealthy)"
)

# ========== Application Setup ==========
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8000"))

VISITS_FILE = "visits.txt"


def get_visit_count():
    """Retrieve the current visit count from the file."""
    if not os.path.exists(VISITS_FILE):
        return 0
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip())
    except ValueError:
        return 0


def update_visit_count():
    """Increment and update the visit count in the file."""
    count = get_visit_count() + 1
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))
    return count


def create_flask_app() -> Flask:
    """
    Creates an application and configures routes
    """
    app = Flask(__name__)
    time_format = "%H:%M:%S %d.%m.%Y"

    @app.route("/")
    def show_moscow_time():
        """
        Returns an html page with current time in Moscow
        """

        # Update visits counter
        update_visit_count()

        # Get the timezone and current time
        moscow_tz = pytz.timezone("Europe/Moscow")
        moscow_time = datetime.now(moscow_tz).strftime(time_format)

        # Pass the time to the HTML template
        return render_template("moscow_time.html", moscow_time=moscow_time)

    @app.route("/metrics")
    def metrics():
        return Response(
            generate_latest(REGISTRY), 200, {"Content-Type": "text/plain"}
        )

    @app.route("/health")
    def health_check():
        HEALTH_GAUGE.set(1)
        return "OK", 200

    @app.route("/visits")
    def visits():
        """Returns the number of recorded visits."""
        return {"visits": get_visit_count()}, 200

    return app


wsgi_app = create_flask_app()


if __name__ == "__main__":
    wsgi_app.run(host=HOST, port=PORT, debug=False)
