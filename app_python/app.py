from datetime import datetime
import pytz
from flask import Flask, Response
from prometheus_client import generate_latest, start_http_server, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)
# Define a counter metric for tracking requests
REQUEST_COUNT = Counter('python_app_requests_total', 'Total number of requests')

@app.route("/")
def show_time():
    REQUEST_COUNT.inc()  # Increment counter each time endpoint is called
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time in Moscow: {current_time}</h1>"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
start_http_server(8000)