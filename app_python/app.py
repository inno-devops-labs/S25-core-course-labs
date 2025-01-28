from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def moscow_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time in Moscow: {current_time}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
