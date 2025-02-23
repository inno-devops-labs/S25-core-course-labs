from datetime import datetime, timezone, timedelta
from flask import Flask, render_template, request
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
    moscow_tz = timezone(timedelta(hours=3))  # Moscow timezone is UTC +3
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    return render_template('time_request.html', time=moscow_time)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
