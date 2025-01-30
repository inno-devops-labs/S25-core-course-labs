from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time in Moscow</h1><p>{moscow_time}</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)