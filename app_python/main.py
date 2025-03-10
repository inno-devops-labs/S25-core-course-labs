from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# Where we'll store our persistent visits count
VISITS_FILE = "/app/data/visits"


def read_visits():
    """
    Reads the current visits count from VISITS_FILE.
    Returns 0 if the file does not exist.
    """
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, "r") as f:
        content = f.read().strip()
        return int(content) if content else 0


def write_visits(count):
    """
    Writes the updated visits count to VISITS_FILE.
    """
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


@app.route("/")
def show_time():
    """
    Increments the visits counter and displays the current time in Moscow (MSK).
    """
    # 1. Read current visits count
    visits = read_visits()
    # 2. Increment
    visits += 1
    # 3. Save the updated visits
    write_visits(visits)

    # Retrieve the current time in Moscow
    tz_moscow = pytz.timezone("Europe/Moscow")
    time_msk = datetime.now(tz_moscow).strftime("%Y-%m-%d %H:%M:%S")

    return f"""
        <h1>Current time in Moscow: {time_msk}</h1>
        <p>You are visitor number: {visits}</p>
    """


@app.route("/visits")
def visits():
    """
    Displays the total visits recorded so far.
    """
    total_visits = read_visits()
    return f"<h2>Total visits so far: {total_visits}</h2>"


if __name__ == "__main__":
    # Keep same port, just updated logic
    app.run(host="0.0.0.0", port=5050)
