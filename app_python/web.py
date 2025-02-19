"""
Flask application for displaying the current time in Moscow
"""

import logging
from datetime import datetime
from flask import Flask, render_template, jsonify
import pytz


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


def get_moscow_time():
    """
    Current MSK Time
    """
    moscow_tz = pytz.timezone("Europe/Moscow")
    return datetime.now(moscow_tz).strftime("%H:%M:%S")


@app.route("/ct")
def get_time():
    """
    Used to get MSK time and use it in script.js file
    """
    return jsonify({"ct": get_moscow_time()})


@app.route("/")
def index():
    """
    Displays the current time in Moscow
    """
    logging.info("Main page with timezone was loaded")
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    return render_template("index.html", time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
