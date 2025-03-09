from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz
import os

app = Flask(__name__)

VISITS_FILE = 'visits.txt'

def get_moscow_time():
    tz = pytz.timezone("Europe/Moscow")
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

def get_visit_count():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            count = file.read()
            if count.isdigit():
                return int(count)
    return 0  

def increment_visit_count():
    count = get_visit_count() + 1
    with open(VISITS_FILE, 'w') as file:
        file.write(str(count))
    return count

@app.route('/')
def home():
    increment_visit_count() 
    return render_template('index.html')

@app.route('/time')
def get_time():
    return jsonify(time=get_moscow_time())

@app.route('/visits')
def visits():
    count = get_visit_count()
    return jsonify(visits=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# requirements.txt
# Flask
# pytz
