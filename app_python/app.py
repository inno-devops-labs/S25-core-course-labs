from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)

VISITS_FILE = './visits.txt'

def update_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            content = file.read().strip()
            visits = int(content) if content else 0  # Handle empty file case
    else:
        visits = 0

    visits += 1

    with open(VISITS_FILE, 'w') as file:
        file.write(str(visits))

    return visits

@app.route("/")
def show_time():
    update_visits()
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    return f"<h1>Current Time in Moscow: {moscow_time.strftime('%Y-%m-%d %H:%M:%S')}</h1>"

@app.route("/visits")
def show_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            visits = file.read().strip()
    else:
        visits = 0
    return f"<h1>Number of visits: {visits}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
