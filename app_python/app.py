"""
This module contains the Flask application for displaying
the current time in Moscow and tracking the number of
visits using Prometheus metrics.
"""
from datetime import datetime
from flask import Flask, render_template
from pytz import timezone
from prometheus_client import start_http_server, Counter

VISITS_FILE = "visits"

# Create a counter metric to track requests
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')


def read_visits():
    """Read the number of visits from the file."""
    try:
        with open(VISITS_FILE, "r", encoding="utf-8") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def write_visits(count):
    """Write the number of visits to the file."""
    with open(VISITS_FILE, "w", encoding="utf-8") as file:
        file.write(str(count))


def create_app():
    """
    Create and configure the Flask app.
    Returns:
        Flask app instance.
    """
    app = Flask(__name__)

    # Start the Prometheus metrics server on port 5001
    start_http_server(5001)

    @app.route('/')
    def show_moscow_time():
        """
        Function to display the current time in Moscow timezone.
        Returns:
            Rendered HTML template with the current time in Moscow.
        """
        # Increment the request counter
        REQUEST_COUNT.inc()

        # Increment visit counter
        visits = read_visits() + 1
        write_visits(visits)

        # Get the current time in the Moscow timezone
        moscow_tz = timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

        # Render the template with the current time
        return render_template('index.html', current_time=current_time)

    @app.route('/visits')
    def visit_count():
        """Display the number of visits recorded."""
        visits = read_visits()
        return render_template('visits.html', visits=visits)

    return app


# Run the application only if executed directly
if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run()
