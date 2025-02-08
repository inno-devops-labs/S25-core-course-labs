from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def home():
    try:
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
        return render_template("index.html", time=moscow_time)
    except Exception as e:
        return e, 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
