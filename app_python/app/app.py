"""
This is a python web application using Flask framework that shows current time in Moscow.
"""

from datetime import datetime, timezone, timedelta

from flask import Flask, render_template

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

    return render_template("index.html", time=time_str)


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
