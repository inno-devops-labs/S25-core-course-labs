from app_python.app import app
from flask import render_template
from datetime import datetime
import pytz

@app.route('/')
def moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time_now = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time_now)
