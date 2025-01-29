from datetime import datetime
import pytz
from flask import Flask, render_template

TIMEZONE = "Europe/Moscow"
PAGE = "index.html"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Returns html page that displays time in Moscow
    """
    time = datetime.now(pytz.timezone(TIMEZONE))
    return render_template(PAGE, time=time)

if __name__ == "__main__":
    app.run()