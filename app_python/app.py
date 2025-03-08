from flask import Flask, render_template, jsonify
import os
from datetime import datetime
from prometheus_client import start_http_server, Counter, generate_latest, CONTENT_TYPE_LATEST
import threading
import pytz

app = Flask(__name__)
VISITS_FILE = 'data/visits'
request_count = Counter('http_requests_total', 'Total number of HTTP requests')

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route("/health")
def health():
    return "OK", 200

def get_visits():
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, 'r') as f:
        try:
            return int(f.read().strip())
        except ValueError:
            return 0


def update_visits():
    visits = get_visits() + 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(visits))
    return visits

@app.route('/visits')
def visits_endpoint():
    visits = get_visits()
    return jsonify({"visits": visits})

@app.route("/")  
def index():
    visits = update_visits()
    request_count.inc()

    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
    
    return render_template("index.html", time=current_time, visits=visits)

def start_prometheus():
    start_http_server(7000) 

if __name__ == "__main__":
    threading.Thread(target=start_prometheus, daemon=True).start()
    
    app.run(host="0.0.0.0", port=5001)
