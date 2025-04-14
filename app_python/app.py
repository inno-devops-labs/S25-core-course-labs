from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


# function to get the time using pytz (timezone)
@app.route('/')
def get_time():
    timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Current time in Moscow, Russia:</h1><p>{moscow_time}</p>"


# run the application on the local server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
