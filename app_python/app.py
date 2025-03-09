from flask import Flask, render_template
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

import os
import pytz


app = Flask(__name__)
metrics = PrometheusMetrics(app)
# automatically exports metrics to /metrics

# global vars that represent a city to display time in
CITY = "Moscow"
TIMEZONE = "Europe/Moscow"

HOST = '0.0.0.0'
PORT = 5000

VISITS_DIR = "data"
VISITS_FILE = "data/visits"


def get_visits():
    try:
        with open(VISITS_FILE, "r") as f:
            data = f.read()
            return int(data)
    except Exception as e:
        print("Error while getting visits: ", e)
        return -1


def set_visits(visits):
    try:
        if VISITS_DIR is not None:
            os.makedirs(VISITS_DIR, exist_ok=True)
        with open(VISITS_FILE, "w") as f:
            f.write(str(visits))
    except Exception as e:
        print("Error while setting visits: ", e)


def visit_page():
    if not os.path.isfile(VISITS_FILE):
        print(f"File {VISITS_FILE} doesn't exist, creating it with value 0")
        f = open(VISITS_FILE, "w")
        f.write("0")
        f.close()

    visits = get_visits()
    if visits >= 0:
        set_visits(visits + 1)
    else:
        print("Cannot get visits")
        set_visits(visits)


# function for returning date and time in the given timezone
def get_current_time(str_timezone):
    try:
        tz = pytz.timezone(str_timezone)
        return datetime.now(tz)
    except pytz.UnknownTimeZoneError:
        app.logger.error(f"Unknown time zone: {str_timezone}")
        return None


def set_new_timezone(new_tz):
    global TIMEZONE
    TIMEZONE = new_tz


# rendering the home (main) page
@app.route('/')
@metrics.counter('homepage_requests', 'Requests to homepage')
def home():
    visit_page()
    localized_time = get_current_time(TIMEZONE)
    if localized_time is None:
        return "Invalid given timezone", 400

    cur_time = localized_time.strftime('%d/%m/%Y %H:%M:%S')

    return render_template('home.html', cur_time=cur_time, city=CITY)


@app.route('/health')
def health():
    return "OK", 200


@app.route('/visits')
def retrieve_visits():
    page_content = f"Number of page visits: {get_visits()}"
    return page_content, 200


if __name__ == '__main__':
    app.run(debug=False, host=HOST, port=PORT)
