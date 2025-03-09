import os
from datetime import datetime, timezone, timedelta

from flask import Flask, render_template, Response

app = Flask(__name__)
visits_file = "visits.txt"


def increment_visit_count():
    try:
        if os.path.exists(visits_file):
            with open(visits_file, 'r+') as file:
                count = int(file.read().strip()) + 1
                file.seek(0)
                file.write(str(count))
                file.truncate()
        else:
            with open(visits_file, 'w') as file:
                count = 1
                file.write(str(count))
        return count
    except Exception as e:
        return str(e)


@app.route("/")
def index():
    moscow_time = (datetime.utcnow().replace(tzinfo=timezone.utc) +
                   timedelta(hours=3))
    increment_visit_count()
    return render_template("index.html",
                           time=moscow_time.strftime("%Y-%m-%d %H:%M:%S"))


@app.route("/visits")
def visits():
    try:
        with open(visits_file, 'r') as file:
            visit_num = file.read().strip()
    except FileNotFoundError:
        visit_num = "0"
    return Response(f"Total visits: {visit_num}", mimetype='text/plain')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
