import logging
from datetime import datetime
from flask import Flask, render_template
import pytz
import os

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

VISITS_FILE = 'visits.txt'

def read_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            count = file.read()
            return int(count)
    else:
        return 0

def write_visits(count):
    with open(VISITS_FILE, 'w') as file:
        file.write(str(count))

@app.route("/")
def current_time():
    """
    Function to display the current time in Moscow
    """
    tz_moscow = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(tz_moscow).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Served current time: {moscow_time}")
    return render_template("index.html", time=moscow_time)

@app.route("/visits")
def visits():
    """
    Function to display the number of visits
    """
    count = read_visits()
    count += 1
    write_visits(count)
    logging.info(f"Visit count updated: {count}")
    return render_template("visits.html", count=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
