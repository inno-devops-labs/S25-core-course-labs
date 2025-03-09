"""
This is a python web application using Flask framework that shows current time in Moscow.
"""

from datetime import datetime, timezone, timedelta

import os

import logging

from pathlib import Path
from flask import Flask, render_template

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

web_app = Flask(__name__)

VISITS_FILE = 'visits.txt'

def get_visits_file_path():
    file_path = os.environ.get('VISITS_FILE', VISITS_FILE)
    # Ensure directory exists
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    return file_path


def get_visits():
    try:
        file_path = get_visits_file_path()
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return int(f.read().strip() or '0')
        return 0
    except (FileNotFoundError, ValueError):
        return 0


def increment_visits():
    visit_count = get_visits() + 1
    with open(get_visits_file_path(), 'w') as f:
        f.write(str(visit_count))
    return visit_count

@web_app.route("/")
def index():
    """
    Returns rendered template with current time in Moscow timezone
    """
    utc_now = datetime.now(timezone.utc)
    moscow_tz = timezone(timedelta(hours=3))
    moscow_time = utc_now.astimezone(moscow_tz)
    increment_visits()
    time_str = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

    logging.info(f"Served current time: {time_str}")

    return render_template("index.html", time=time_str)


@web_app.route("/visits")
def show_visits():
    visits = get_visits()
    return {"visits": visits}

if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
