from flask import Flask, request
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show():
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return f'Current Moscow time: {moscow_time}'

visit_count = 0

@app.route('/visits')
def visits():
    global visit_count
    visit_count += 1  # Increment the visit counter
    
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    
    # Log visit details
    visitor_ip = request.remote_addr
    visit_message = f'Current Moscow time: {moscow_time}. Total visits: {visit_count}. Visitor IP: {visitor_ip}'
    
    return visit_message

if __name__ == '__main__':

    app.run('0.0.0.0', ssl_context='adhoc')
