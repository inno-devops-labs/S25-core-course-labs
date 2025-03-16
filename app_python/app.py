from flask import Flask, render_template
from datetime import datetime
import pytz
import os

app = Flask(__name__)

VISITS_FILE = 'visits'  # File to store visit count


def get_moscow_time():
    """Fetches the current time in Moscow timezone."""
    moscow_tz = pytz.timezone('Europe/Moscow')
    return datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')


def get_visit_count():
    """Reads the visit count from the file. If the file doesn't exist, initializes it."""
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            return int(file.read().strip())
    else:
        # If the file doesn't exist, initialize it with 0
        return 0


def save_visit_count(count):
    """Saves the current visit count to the file."""
    with open(VISITS_FILE, 'w') as file:
        file.write(str(count))

@app.route('/')
def home():
    """Renders the main page displaying Moscow time and increments the visit counter."""
    visit_count = get_visit_count() + 1
    save_visit_count(visit_count)
    
    current_time = get_moscow_time()
    return render_template('index.html', time=current_time, visit_count=visit_count)



@app.route('/visits')
def visits():
    """Displays the recorded number of visits."""
    visit_count = get_visit_count()
    return f'This site has been visited {visit_count} times.'


if __name__ == '__main__':
    app.run(debug=True)
