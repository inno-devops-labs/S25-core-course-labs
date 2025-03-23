import os
from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


def get_counter_file():
    return os.getenv("COUNTER_FILE", "/app/data/visits.txt")


@app.route('/')
def time():
    counter_file = get_counter_file()

    os.makedirs(os.path.dirname(counter_file), exist_ok=True)

    count = 0
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            count = int(f.read().strip())

    count += 1
    with open(counter_file, "w") as f:
        f.write(str(count))

    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%dT%H:%M:%S')
    return render_template('index.html', moscow_time=moscow_time)


@app.route('/visits')
def visits():
    counter_file = get_counter_file()

    count = 0
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            count = int(f.read().strip())
    return jsonify(visits=count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
