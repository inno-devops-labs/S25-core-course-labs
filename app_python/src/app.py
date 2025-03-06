from flask import Flask, render_template
from datetime import datetime
import pytz
import os


def create_app():
    app = Flask(__name__)
    VISITS_FILE = "src/data/visits.txt"
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")

    @app.route('/')
    def home():
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

        with open(VISITS_FILE, "r+") as f:
            visits = int(f.read()) + 1
            f.seek(0)
            f.write(str(visits))

        return render_template('index.html',
                               current_time=current_time,
                               visits=visits)

    @app.route('/visits')
    def show_visits():
        with open(VISITS_FILE, "r") as f:
            visits = f.read()
        return f"Total visits: {visits}"

    return app
