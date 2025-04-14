from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def show():
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return f'Current Moscow time: {moscow_time}'


if __name__ == '__main__':

    app.run('0.0.0.0', ssl_context='adhoc')
