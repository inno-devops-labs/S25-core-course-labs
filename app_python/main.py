from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def show_time():
    """
    Displays the current time in Moscow (MSK).
    """
    tz_moscow = pytz.timezone("Europe/Moscow")
    time_msk = datetime.now(tz_moscow).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current time in Moscow: {time_msk}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
