from datetime import datetime
import pytz
from flask import Flask, render_template, Response
from prometheus_client import Counter, generate_latest

METRIC_REQUESTS = Counter("app_requests_total", "Total Requests")


def create_app():
    app_py = Flask(__name__)
    return app_py


app = create_app()


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


@app.route('/')
def moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time_now = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time_now)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
