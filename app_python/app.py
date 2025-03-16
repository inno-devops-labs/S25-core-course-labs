from flask import Flask, render_template_string
from datetime import datetime
import pytz
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

VISITS_FILE = "visits"


def some_function(x):
    return x * x


def get_visits():
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, "r") as f:
        try:
            return int(f.read().strip())
        except ValueError:
            return 0


def save_visits(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


@app.route("/metrics")
def metrics_endpoint():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


@app.route("/")
def home():
    visits = get_visits() + 1
    save_visits(visits)

    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Moscow Time</title>
        </head>
        <body>
            <h1>Current Time in Moscow</h1>
            <p>{{ time }}</p>
        </body>
        </html>
        """,
        time=moscow_time,
    )


@app.route("/visits")
def visits():
    return f"This page has been visited {get_visits()} times."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
