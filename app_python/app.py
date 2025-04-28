from flask import Flask, jsonify, render_template
from datetime import datetime
import pytz
import os

VISITS_FILE = "visits.txt"


def create_app():
    _app = Flask(__name__)
    return _app


app = create_app()


def get_current_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    return datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')


def read_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0


def write_visits(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    current_time = get_current_time()
    write_visits(read_visits() + 1)
    return jsonify(time=current_time)


@app.route('/visits')
def visits():
    count = read_visits() + 1
    write_visits(count)
    return jsonify(visits=count)


if __name__ == '__main__':
    if not os.path.exists(VISITS_FILE):
        write_visits(0)
    app.run(host="0.0.0.0", port=8080)
