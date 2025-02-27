from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def moscow_time():
    tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(tz)

    data = {
        "timezone": tz.zone,
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
