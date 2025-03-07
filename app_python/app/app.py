import os
from datetime import datetime

import pytz
from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, render_template

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8080"))
VISITS_FILE = os.environ.get("VISITS_FILE", "app/data/visits.txt")


def increment_visits():
    with open(VISITS_FILE, "r") as file:
        v = int(file.read())

    with open(VISITS_FILE, "w") as file:
        file.write(str(v + 1))


def create_app():
    """
    Creates an app and configures env.
    """

    app = Flask(__name__)
    metrics = PrometheusMetrics(app)
    metrics.info("app_info", "Application info", version="1.0.0")

    if not os.path.isfile(VISITS_FILE):
        parent_dir = os.path.join(VISITS_FILE, os.pardir)
        os.makedirs(os.path.abspath(parent_dir), exist_ok=True)

        with open(VISITS_FILE, "w") as file:
            file.write("0")

    @app.route("/", methods=["GET"])
    def index():
        """
        Returns html page with current Moscow time.
        """
        moscow_timezone = pytz.timezone("Europe/Moscow")
        time = datetime.now(moscow_timezone)
        return render_template("index.html", time=time)

    @app.route("/visits", methods=["GET"])
    def visits():
        """
        Returns total number of visits.
        """
        with open(VISITS_FILE, "r") as file:
            return {"visits": int(file.read())}

    return app


app = create_app()

if __name__ == "__main__":
    print(os.getcwd())
    app.run(host=HOST, port=PORT)
