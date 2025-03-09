from flask import Flask, render_template
from datetime import datetime
import pytz
import logging
import os


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

VISITS_FILE = '/data/visits.txt'

if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, 'w') as f:
        f.write('0')


@app.route('/')
def home():
    with open(VISITS_FILE, 'r') as f:
        current_count = int(f.read().strip() or 0)
        new_count = current_count + 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(new_count))
        f.truncate()

    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    app.logger.info(f'Time: {moscow_time} | Total visits: {new_count}')

    return render_template('index.html', 
                         time=moscow_time,
                         visits=new_count)


@app.route('/visits')
def show_visits():
    with open(VISITS_FILE, 'r') as f:
        count = f.read().strip()
    return f'Total visits: {count}'


if __name__ == '__main__':
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
    app.run(host='0.0.0.0', port=5000)

