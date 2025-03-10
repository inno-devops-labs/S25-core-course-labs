from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

VISITS_FILE = "/data/visits.txt"

def get_visits():
    try:
        with open(VISITS_FILE, 'r') as f:
            return int(f.read() or 0)
    except:
        return 0

def save_visits(count):
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))

@app.route('/')
def home():
    visits = get_visits() + 1
    save_visits(visits)
    return f'Hello! Current time is {datetime.now()}'

@app.route('/visits')
def visits():
    return f'Total visits: {get_visits()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 