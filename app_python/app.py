"""
Python web application that displays the current time in Moscow
"""

from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)


@app.route("/")
def current_time():
    """
    Function to display the current time in Moscow
    """
    tz_moscow = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(tz_moscow).strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", time=moscow_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
