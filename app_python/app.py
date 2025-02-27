from flask import Flask
from datetime import datetime
import pytz


# Flask initialization
app = Flask(__name__)


# Endpoint for time checking
@app.route("/")
def check_time():
    msc_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(msc_tz).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current time in Moscow: {current_time}</h1>"


# Starting the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
