from flask import Flask
from flask import render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def show_moscow_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz)
    moscow_time_str = moscow_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    return render_template("index.html", time=moscow_time_str)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
