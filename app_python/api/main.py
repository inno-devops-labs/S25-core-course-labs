from datetime import datetime
from flask import Flask, render_template
import pytz
import os

VISITS_FILE = "visits.txt"


def increment_counter():
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'w') as f:
            f.write("0")
    with open(VISITS_FILE, 'r') as f:
        count_str = f.read().strip()
        count = int(count_str) if count_str.isdigit() else 0
    count += 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))
    return count


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        try:
            increment_counter()
            moscow_tz = pytz.timezone('Europe/Moscow')
            moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
            return render_template("index.html", time=moscow_time)
        except Exception as e:
            return e, 500

    @app.route("/visits")
    def visits():
        try:
            if not os.path.exists(VISITS_FILE):
                count = 0
            else:
                with open(VISITS_FILE, 'r') as f:
                    count_str = f.read().strip()
                    count = int(count_str) if count_str.isdigit() else 0
            return f"Total visits: {count}"
        except Exception as e:
            return str(e), 500

    return app


if __name__ == "__main__":
    main_app = create_app()
    main_app.run(debug=True, host='0.0.0.0', port=5000)
