from flask import Flask
from datetime import datetime
import pytz
from prometheus_client import start_http_server, Counter, generate_latest

METRIC_REQUESTS = Counter("app_requests_total", "Total number of requests")

app = Flask(__name__)

@app.route("/")
def home():
    METRIC_REQUESTS.inc()
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    return f"<h1>Current Time in Moscow</h1><p>{moscow_time}</p>"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; version=0.0.4; charset=utf-8"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)