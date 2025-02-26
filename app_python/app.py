from flask import Flask
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Gauge
from datetime import datetime
import pytz

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')
LAST_METRICS_ACCESS = Gauge('app_last_metrics_access_time', 'Last time the /metrics endpoint was accessed')


@app.route("/")
def moscow_time():
    REQUEST_COUNT.inc()
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current time in Moscow is {current_time}</h1>"


@app.route("/metrics")
def metrics():
    LAST_METRICS_ACCESS.set_to_current_time()
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
