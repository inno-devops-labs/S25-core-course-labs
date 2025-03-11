from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# Файл для хранения счетчика
VISITS_FILE = "/data/visits"

if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")


@app.route("/")
def home():
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    # Увеличиваем счетчик
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
