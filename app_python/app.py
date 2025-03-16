import os
from datetime import datetime, timezone, timedelta
from flask import Flask, render_template, request
from flask.json import jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)  # from https://pypi.org/project/prometheus-flask-exporter/

@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status

@app.route('/')
def time_request():
    visit()
    moscow_tz = timezone(timedelta(hours=3))  # Moscow timezone is UTC +3
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    return render_template('time_request.html', time=moscow_time)

def visit():
    if not os.path.exists("/data/visits.txt"):
        os.makedirs("/data", exist_ok=True)
        with open("/data/visits.txt", "w") as file:
            file.write("0")
    with open("/data/visits.txt", "r") as file:
        v = int(file.read())
    with open("/data/visits.txt", "w") as file:
        file.write(str(v + 1))

@app.route('/visits')
def visits_request():
    visit()
    with open("/data/visits.txt", "r") as file:
        return jsonify(content={"visits": int(file.read())})


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
