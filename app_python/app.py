from flask import Flask, jsonify, render_template
from datetime import datetime
import pytz
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app, group_by='endpoint')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/time")
def get_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
    return jsonify({"time": moscow_time})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec
