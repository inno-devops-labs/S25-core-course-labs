from flask import Flask
from flask import render_template
from datetime import datetime
import pytz

app = Flask(__name__)

visits_path = "/app/visits"


@app.route("/")
def show_moscow_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz)
    moscow_time_str = moscow_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    return render_template("index.html", time=moscow_time_str)


@app.route('/visits')
def visits():
    current_count = get_visit_count()
    count = increment_visit_count(current_count)

    return render_template("visits.html", visits=count)


def get_visit_count():
    try:
        with open(visits_path, 'r') as f:
            return int(f.read().strip() or '0')
    except FileNotFoundError:
        return 0


def increment_visit_count(current_count):
    try:
        with open(visits_path, 'w') as f:
            f.write(str(current_count + 1))
        return current_count + 1
    except Exception as e:
        print(f"Error incrementing visit count: {e}")
        return current_count


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
