import datetime
from flask import Flask, render_template
from app import app

@app.route('/')
def current_time():
    moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))  # Moscow Timezone
    moscow_time = datetime.datetime.now(moscow_timezone)
    return render_template('index.html', current_time=moscow_time)
