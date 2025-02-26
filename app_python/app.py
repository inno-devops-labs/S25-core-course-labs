from flask import Flask, render_template
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

import pytz


app = Flask(__name__)
metrics = PrometheusMetrics(app)
# automatically exports metrics to /metrics

# global vars that represent a city to display time in
CITY = "Moscow"
TIMEZONE = "Europe/Moscow"

HOST = '0.0.0.0'
PORT = 5000


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
    localized_time = get_current_time(TIMEZONE)
    if localized_time is None:
        return "Invalid given timezone", 400

    cur_time = localized_time.strftime('%d/%m/%Y %H:%M:%S')

    return render_template('home.html', cur_time=cur_time, city=CITY)


@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(debug=False, host=HOST, port=PORT)
