"""
Python web application that displays the current time in Moscow
"""

import logging
from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@app.route("/")
def current_time():
    """
    Function to display the current time in Moscow
    """
    tz_moscow = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(tz_moscow).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Served current time: {moscow_time}")
    return render_template("index.html", time=moscow_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
