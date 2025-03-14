"""
Flask application for displaying the current time in Moscow
"""

import logging
from datetime import datetime
from flask import Flask, render_template, jsonify
import pytz
import os


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
VISITS_FILE = "/app_python/visits.txt"


def get_moscow_time():
    """
    Current MSK Time
    """
    moscow_tz = pytz.timezone("Europe/Moscow")
    return datetime.now(moscow_tz).strftime("%H:%M:%S")


def inc_visits():
    """
    Read visit count from file, increment and update
    """
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")
    
    with open(VISITS_FILE, "r+") as f:
        count = int(f.read().strip())
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    return count


def get_visit_count():
    """
    Get current visit count from file
    """
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")
    
    with open(VISITS_FILE, "r+") as f:
        return int(f.read().strip())


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
    current_time = get_moscow_time()
    inc_visits()

    return render_template("index.html", time=current_time)


@app.route("/visits")
def visits():
    """
    Displays the visit count
    """
    count = get_visit_count()
    return jsonify({"visits": count})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
