from flask import Flask, jsonify, Response
from datetime import datetime
import pytz
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)

REQUEST_COUNT = Counter("request_count", "Requests Counter", ["method", "endpoint"])


@app.route("/")
def moscow_time():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()

    tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(tz)

    data = {
        "timezone": tz.zone,
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    return jsonify(data)


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
