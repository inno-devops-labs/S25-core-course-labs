from flask import Flask, jsonify
from datetime import datetime
import pytz
import os

app = Flask(__name__)
VISITS_FILE = "visits.txt"

def read_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

def write_visits(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))

@app.route('/')
def get_moscow_time():
    # Get Moscow timezone and the current time
    msk_time_zone = pytz.timezone('Europe/Moscow')
    msk_current_time = datetime.now(msk_time_zone).strftime('%H:%M:%S')
    count = read_visits() + 1
    write_visits(count)

    # Show the current time on the page
    return f"<h2>The current time in Moscow:</h2><h1>{msk_current_time}</h1>"

@app.route('/visits')
def visits():
    # Increment the counter stored in the visits file
    count = read_visits() + 1
    write_visits(count)
    return jsonify({"visits": count})

if __name__ == '__main__':
    if not os.path.exists(VISITS_FILE):
        write_visits(0)
    app.run(debug=True, host='0.0.0.0', port=5000)
