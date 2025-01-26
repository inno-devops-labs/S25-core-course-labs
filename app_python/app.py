from datetime import datetime

import pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Returns html page with current Moscow time.
    """
    moscow_timezone = pytz.timezone('Europe/Moscow')
    time = datetime.now(moscow_timezone)
    return render_template("index.html", time=time)


if __name__ == "__main__":
    app.run()
