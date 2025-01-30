from flask import Flask, jsonify, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


def get_current_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    return datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    current_time = get_current_time()
    return jsonify(time=current_time)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
