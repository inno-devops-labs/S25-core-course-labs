from flask import Flask, render_template
from datetime import datetime
import pytz
import os

app = Flask(__name__)

VISITS_FILE = 'visits.txt'


def get_moscow_time():
    """Fetches the current time in Moscow timezone."""
    moscow_tz = pytz.timezone('Europe/Moscow')
    return datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')


def update_visit_counter():
    """Reads the current visit count, increments it, and saves it back."""
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            count = int(file.read())
    else:
        count = 0

    count += 1

    with open(VISITS_FILE, 'w') as file:
        file.write(str(count))
    return count


@app.route('/')
def home():
    """Renders the main page displaying Moscow time."""
    current_time = get_moscow_time()
    # Update visit counter and pass it to the template
    visit_count = update_visit_counter()
    return render_template('index.html', time=current_time, visit_count=visit_count)


@app.route('/visits')
def visits():
    """Displays the recorded visits from the file."""
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            visit_count = int(file.read())
    else:
        visit_count = 0
    return f'The site has been visited {visit_count} times.'


if __name__ == '__main__':
    app.run(debug=True)
