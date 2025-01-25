from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)


@app.route("/")
def current_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current time in Moscow: {current_time}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
