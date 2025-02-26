from flask import Flask
from datetime import datetime
import pytz
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def show_time():
    msc_t = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(msc_t).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Current time in Moscow: {moscow_time}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
