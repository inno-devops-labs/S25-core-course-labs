from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)
VISITS_FILE = "visits"


def get_visit_count():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "r") as file:
            return int(file.read().strip())
    return 0


def increment_visit_count():
    count = get_visit_count() + 1
    with open(VISITS_FILE, "w") as file:
        file.write(str(count))


@app.route("/")
def get_moscow_time():
    """Returns the time in Europe/Moscow timezone"""

    tz_moscow = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(tz_moscow).strftime("%H:%M:%S")
    increment_visit_count()
    html_content = f"""
    <html>
        <body>
            <h3>Time in Moscow - {moscow_time}</h3>
        </body>
    </html>
    """
    return html_content


@app.route("/visits")
def get_visits():
    """Returns the number of visits"""
    count = get_visit_count()
    increment_visit_count()
    html_content = f"""
    <html>
        <body>
            <h3>Number of visits - {count}</h3>
        </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
