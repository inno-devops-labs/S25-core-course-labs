import datetime
from flask import render_template
from app import app


@app.route('/')
def current_time():
    moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(moscow_timezone)
    return render_template('index.html', current_time=moscow_time)
