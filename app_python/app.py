from flask import Flask, Response
from datetime import datetime
import pytz
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

app = Flask(__name__)

# Define Prometheus counter for tracking HTTP requests
REQUEST_COUNT = Counter(
    "http_requests_total", "Total number of HTTP requests", ["method", "endpoint"]
)

@app.route("/")
def show_time():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()  # Increment counter
    
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    
    return f"<h1>Current Time in Moscow: {moscow_time}</h1>"

@app.get("/metrics")
def metrics():
    REQUEST_COUNT.labels(method="GET", endpoint="/metrics").inc()  # Increment counter
    
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
