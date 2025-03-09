from datetime import datetime
import pytz
import os
from flask import Flask, jsonify

app = Flask(__name__)

VISITS_FILE = '/data/visits.txt'

def get_moscow_time():
    try:
        return datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"Error fetching Moscow time: {e}")
        return "Error fetching Moscow time"

def read_visits():
    try:
        with open(VISITS_FILE, 'r') as f:
            return int(f.read().strip())
    except Exception:
        return 0

def write_visits(count):
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))

@app.route('/')
def home():
    moscow_time = get_moscow_time()
    return f"<h1>Current time in Moscow: {moscow_time}</h1>"

@app.route('/visits')
def visits():
    count = read_visits()
    count += 1
    write_visits(count)
    return jsonify({"visits": count})

@app.errorhandler(404)
def not_found(error):
    return "<h1>404 - Page Not Found</h1><p>The requested URL was not found on the server.</p>", 404

if __name__ == '__main__':
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
    app.run(debug=True, host='127.0.0.1', port=5001)
