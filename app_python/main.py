from datetime import datetime
from flask import Flask, render_template

import pytz

app = Flask(__name__)


@app.route("/")
def get_time():
    try:
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')
        return render_template("index.html", time=moscow_time)
    except Exception as e:
        return "Internal server error", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9200)
