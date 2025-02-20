"""
This is a python web application using Flask framework that shows current time in Moscow.
"""

from datetime import datetime, timezone, timedelta

import logging

from flask import Flask, render_template

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

web_app = Flask(__name__)


@web_app.route("/")
def index():
    """
    Returns rendered template with current time in Moscow timezone
    """
    utc_now = datetime.now(timezone.utc)
    moscow_tz = timezone(timedelta(hours=3))
    moscow_time = utc_now.astimezone(moscow_tz)

    time_str = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

    logging.info(f"Served current time: {time_str}")

    return render_template("index.html", time=time_str)


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
