from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    # Set timezone to Moscow
    tz_moscow = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz_moscow).strftime('%Y-%m-%d %H:%M:%S')
    return f"<h1>Current Time in Moscow:</h1><p>{current_time}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)