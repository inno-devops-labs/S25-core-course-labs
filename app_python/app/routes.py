from datetime import datetime

import pytz
from flask import current_app as app, render_template


@app.route('/')
def index():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')

    return render_template('index.html', moscow_time=moscow_time)
