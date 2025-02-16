from datetime import datetime
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import pytz


app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def home():
    """
    Home page of the web app.

    Shows current time in Moscow in format hh:mm:ss dd.mm.yyyy.
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S %d.%m.%Y')
    return render_template('index.html', moscow_time=moscow_time)


if __name__ == '__main__':
    app.run(debug=False)
