from flask import Flask, render_template_string
from datetime import datetime
import pytz
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)
metrics = PrometheusMetrics(app)


def some_function(x):
    return x * x


@app.route("/metrics")
def metrics_endpoint():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route("/")
def home():
    moscow_time = datetime.now(pytz.timezone(
        "Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string("""
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
    """, time=moscow_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
