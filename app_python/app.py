from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Current Time in Moscow:</h1><p>{moscow_time}</p>"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
