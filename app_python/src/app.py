from flask import Flask, render_template
from datetime import datetime
import pytz


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
        return render_template('index.html', current_time=current_time)

    return app
