from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)

VISITS_FILE = "/volume/visits"


def read_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as f:
            return int(f.read().strip())
    return 0


def write_visits(count):
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))


@app.route('/')
def get_time():
    # Increment visit counter
    count = read_visits() + 1
    write_visits(count)

    # Get Moscow time
    timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')

    return f"""
        <h1>Current time in Moscow, Russia:</h1>
        <p>{moscow_time}</p>
        <h2>Visits: {count}</h2>
    """


@app.route('/visits')
def visits():
    count = read_visits()
    return f"Total visits: {count}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
