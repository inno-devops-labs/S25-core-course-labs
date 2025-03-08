from datetime import datetime
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import pytz
import os

PATH_VISITS = 'visits.txt'

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def home():
    """
    Home page of the web app.

    Shows current time in Moscow in format hh:mm:ss dd.mm.yyyy.
    """
    if not os.path.exists(PATH_VISITS):
        with open(PATH_VISITS, 'w') as f:
            f.write("0")

    with open(PATH_VISITS, 'r') as f:
        visits_count = int(f.read())

    visits_count += 1

    with open(PATH_VISITS, 'w') as f:
        f.write(str(visits_count))

    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S %d.%m.%Y')
    return render_template('index.html', moscow_time=moscow_time)


@app.route('/visits')
def visits():
    """
    Visits page of the web app.

    Shows the number of times home page was visited.
    """
    if not os.path.exists(PATH_VISITS):
        with open(PATH_VISITS, 'w') as f:
            f.write("0")

    with open(PATH_VISITS, 'r') as f:
        visits_count = int(f.read())

    return render_template('visits.html', visits=visits_count)


if __name__ == '__main__':
    app.run(debug=False)
