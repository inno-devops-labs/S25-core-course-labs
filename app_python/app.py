import logging
import sys

from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
