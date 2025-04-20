import os
from datetime import datetime
import pytz
from flask import Flask, render_template, Response
from prometheus_client import Counter, generate_latest

METRIC_REQUESTS = Counter("app_requests_total", "Total Requests")
VISITS_FILE = "backup_visits.txt"

def create_app():
    app_py = Flask(__name__)
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")
    return app_py

app = create_app()


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


@app.route('/')
def moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time_now = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    with open(VISITS_FILE, "r+") as f:
        visits = int(f.read().strip() or 0)
        visits += 1
        f.seek(0)
        f.write(str(visits))
        f.truncate()


    return render_template('index.html', time=moscow_time_now)

@app.route('/visits')
def show_visits():
    with open(VISITS_FILE, "r") as f:
        visits = f.read().strip()
    return f"Total visits: {visits}\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
