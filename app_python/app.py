"""Bottle web application that shows the current time and date in Moscow.
Author: Evgeny B.
"""

import os
from datetime import datetime, timedelta, timezone
from bottle import Bottle, response, run
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

# Create a Bottle app instance
app = Bottle()
m_requests = Counter("http_requests_total", "Total HTTP Requests")

# Define the MSK timezone (UTC+3)
MSK_TIMEZONE = timezone(timedelta(hours=3))

VISITS_FILE = "/tmp/visits"


def get_visits():
    """Read the visits count from file."""
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, "r", encoding="utf-8") as visits_file:
        try:
            return int(visits_file.read().strip())
        except ValueError:
            return 0


def update_visits():
    """Increment the visits count and save to file."""
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
    visit_count = get_visits() + 1
    with open(VISITS_FILE, "w", encoding="utf-8") as visits_file:
        visits_file.write(str(visit_count))
    return visit_count


@app.route("/metrics")
def metrics():
    """Expose Prometheus metrics."""
    response.content_type = CONTENT_TYPE_LATEST
    return generate_latest()


@app.route("/")
def show_time():
    """Show the current time and date in Moscow."""
    m_requests.inc()
    visit_count = update_visits()
    # Get the current time in Moscow
    now = datetime.now(MSK_TIMEZONE)
    formatted_time = now.strftime("%H:%M:%S")
    formatted_date = now.strftime("%d.%m.%Y")

    # Set the response content type to HTML
    response.content_type = "text/html; charset=utf-8"
    return (
        f"<html><body><h1>Current time and date in Moscow</h1>"
        f"<p>Time: {formatted_time}</p>"
        f"<p>Date: {formatted_date}</p>"
        f"<p>Visits: {visit_count}</p></body></html>"
    )


@app.route("/visits")
def visits_page():
    """Display the number of visits."""
    response.content_type = "text/plain; charset=utf-8"
    return f"Visits: {get_visits()}\n"


# Run the Bottle app
if __name__ == "__main__":
    # Run the Bottle app on the server
    run(app, host="0.0.0.0", port=8080, debug=False, reloader=False)
