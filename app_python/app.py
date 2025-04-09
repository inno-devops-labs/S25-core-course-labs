"""Flask web application that displays the current time in Moscow and tracks visits."""
from prometheus_client import start_http_server, Summary
from datetime import datetime
import pytz
from flask import Flask, render_template
import os

VISITS_FILE = "data/visits.txt"
os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)

start_http_server(8000)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

app = Flask(__name__)

def read_visits():
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def write_visits(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))

@app.route('/')
def home():
    visits = read_visits() + 1
    write_visits(visits)

    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_time=moscow_time, visits=visits)

@app.route('/visits')
def get_visits():
    count = read_visits()
    return f"Visits: {count}"

if __name__ == '__main__':
    app.run(debug=True)
