from flask import Flask, Response, jsonify
from datetime import datetime
from pytz import timezone
from prometheus_client import generate_latest
import os

app = Flask(__name__)

@app.route("/visits", methods=["GET"])
def get_visits():
    if not os.path.exists('/app/visits.txt'):
        with open('/app/visits.txt', 'w') as f:
            f.write('0')
    with open('/app/visits.txt', 'r') as f:
        visit_count = int(f.readline())
    return jsonify({"visit_count": visit_count})

def save_visit_count():
    if not os.path.exists('/app/visits.txt'):
        with open('/app/visits.txt', 'w') as f:
            f.write('0')
    with open('/app/visits.txt', 'r') as f:
        visit_count = int(f.readline())
    with open('/app/visits.txt', 'w') as f:
        f.write(str(visit_count+1))

@app.route('/')
def show_time():
    save_visit_count()
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    return jsonify({"time": moscow_time})

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
