import logging
import sys

from flask import Flask, render_template, request, Response
from datetime import datetime
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest, Counter, Histogram

from helpers.middlewares import setup_metrics
import pytz

app = Flask(__name__)
setup_metrics(app)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)


@app.before_request
def log_request_info():
    app.logger.info("Received response: %s %s from %s", request.method, request.url, request.remote_addr)


@app.route('/')
def show_moscow_time():
    # Set timezone to Europe/Moscow
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time_moscow = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Render the template with the current time
    return render_template('index.html', current_time=current_time_moscow)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
