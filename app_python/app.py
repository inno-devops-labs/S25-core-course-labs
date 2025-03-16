from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)
visits_file = 'data/visits'


def get_visits():
    if os.path.exists(visits_file):
        with open(visits_file, 'r') as file:
            return int(file.read())
    return 0


def save_visits(count):
    os.makedirs(os.path.dirname(visits_file), exist_ok=True)
    with open(visits_file, 'w') as file:
        file.write(str(count))


@app.route('/visits')
def visits():
    visits = get_visits()
    return f'This page has been visited {visits} times.'


@app.route('/')
def show_time():
    visits = get_visits() + 1
    save_visits(visits)
    print(f"Hello! This page has been visited {visits} times.")
    # Set timezone to Moscow
    tz_moscow = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz_moscow).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Current Time in Moscow:</h1><p>This page has been visited {visits} times.</p>{current_time}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)