from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def current_time_moscow():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return f'Current time in Moscow: {formatted_time}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
