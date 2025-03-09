from flask import Flask, jsonify, render_template
from datetime import datetime
import os
import pytz
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by="endpoint")


@app.route("/")
def index():
    visits_file = '/data/access_count.txt'
    count = 0
    if os.path.exists(visits_file):
        with open(visits_file, 'r') as f:
            count = int(f.read().strip())
    count += 1
    with open(visits_file, 'w') as f:
        f.write(str(count))
    return render_template("index.html")


@app.route("/time")
def get_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
    return jsonify({"time": moscow_time})


@app.route('/visits')
def track_visits():
    visits_file = '/data/access_count.txt'
    count = 0
    if os.path.exists(visits_file):
        with open(visits_file, 'r') as f:
            count = int(f.read().strip())
    return f"Total visits: {count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec
