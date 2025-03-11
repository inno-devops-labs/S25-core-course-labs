from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)

VISITS_FILE = "/data/visits"

if os.path.exists(VISITS_FILE):
    os.chmod(VISITS_FILE, 0o777)
    with open(VISITS_FILE, "w") as f:
        f.write("0")
else:
    fd = os.open(VISITS_FILE, os.O_CREAT | os.O_WRONLY, 0o666)
    os.close(fd)
    os.chmod(VISITS_FILE, 0o777)
    with open(VISITS_FILE, "w") as f:
        f.write("0")


@app.route("/")
def home():
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    with open(VISITS_FILE, "r+") as f:
        count = int(f.read() or 0)
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    return f"Current time in Moscow: {moscow_time}"


@app.route("/visits")
def visits():
    with open(VISITS_FILE, "r") as f:
        count = f.read()
    return f"Number of visits: {count}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
