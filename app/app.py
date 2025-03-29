from flask import Flask
import os

app = Flask(__name__)
visits_path = '/data/visits.txt'

def get_visits():
    if not os.path.exists(visits_path):
        os.makedirs(os.path.dirname(visits_path), exist_ok=True)
        with open(visits_path, 'w') as f:
            f.write('0')
    with open(visits_path, 'r') as f:
        return int(f.read())

def save_visits(count):
    with open(visits_path, 'w') as f:
        f.write(str(count))

@app.route('/')
def home():
    visits = get_visits() + 1
    save_visits(visits)
    return f'Total Visits: {visits}'

@app.route('/visits')
def show_visits():
    return f'Current Visits: {get_visits()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)