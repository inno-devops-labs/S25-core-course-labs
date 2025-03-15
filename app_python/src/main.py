import pytz

from flask import Flask, render_template

from datetime import datetime
import os
import json

COUNTER_OUTPUT = "./data/visits.txt"


# Initialize Flask application
def init_app():
    app = Flask(__name__)

    os.makedirs(os.path.dirname(COUNTER_OUTPUT), exist_ok=True)
    if not os.path.exists(COUNTER_OUTPUT):
        with open(COUNTER_OUTPUT, "w") as f:
            f.write("0")

    @app.route('/')
    def home():
        # Get the current time in Moscow timezone
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
        with open(COUNTER_OUTPUT, "r+") as f:
            visits = int(f.read()) + 1
            f.seek(0)
            f.write(str(visits))

        # Render template with the current time
        return render_template('index.html', current_time=current_time)

    @app.route('/visits')
    def visits():
        with open(COUNTER_OUTPUT, "r") as f:
            visits = f.read()
        return json.dumps({"total_visits": visits})

    return app


if __name__ == '__main__':
    app = init_app()
    app.run(host="0.0.0.0", port=5000)
