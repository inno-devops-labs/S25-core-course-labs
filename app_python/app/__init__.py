from flask import Flask, render_template
from datetime import datetime
import pytz
import os

app = Flask(__name__)

VISITS_FILE = '/data/visits.txt'

os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)

def get_visit():
    try:
        if not os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'w') as f:
                f.write('0')
            return 0

        with open(VISITS_FILE, 'r') as f:
            content = f.read().strip()
            return int(content) if content else 0
    except (IOError, ValueError) as e:
        print(f"Error reading visit count: {e}")
        return 0


def update_visit():
    try:
        count = get_visit() + 1
        with open(VISITS_FILE, 'w') as f:
            f.write(str(count))
        return count
    except IOError as e:
        print(f"Error saving visit count: {e}")
        return 0

@app.route("/")
def show_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    visit_count = update_visit()
    return render_template('index.html', current_time=current_time, visits=visit_count)

@app.route('/visits')
def visits():
    visit_count = get_visit()
    return {'total_visits': visit_count}
