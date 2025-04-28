from flask import Flask, render_template
from datetime import datetime
import pytz
import os

app = Flask(__name__)
VISITS_FILE = "/app/data/visits.txt"  

def get_visits():
    try:
        os.makedirs("/app/data", exist_ok=True)  
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'r') as f:
                content = f.read().strip()
                return int(content) if content else 0
        return 0
    except Exception as e:
        print(f"Error reading visits: {e}")
        return 0

def save_visits(count):
    try:
        with open(VISITS_FILE, 'w') as f:
            f.write(str(count))
    except Exception as e:
        print(f"Error saving visits: {e}")  

@app.route('/')
def home():
    # Increment visit counter
    visits = get_visits() + 1
    save_visits(visits)
    
    # Get the current time in Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time)

@app.route('/visits')
def show_visits():
    visits = get_visits()
    return render_template('visits.html', visits=visits)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")