from datetime import datetime

import pytz
from prometheus_flask_exporter import PrometheusMetrics
from os import environ
from flask import Flask, render_template

HOST = environ.get("HOST", "0.0.0.0")
PORT = int(environ.get("PORT", "8080"))

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0.0")


@app.route("/", methods=["GET"])
def index():
    """
    Returns html page with current Moscow time.
    """
    moscow_timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(moscow_timezone)
    return render_template("index.html", time=time)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
