from flask import Flask
from datetime import datetime
import pytz


# Flask initialization
app = Flask(__name__)

VISITS_FILE = "/data/visits"

def get_visits():
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0


def update_visits(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


# Endpoint for time checking
@app.route("/")
def check_time():
    msc_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(msc_tz).strftime("%Y-%m-%d %H:%M:%S")

    visits = get_visits() + 1
    update_visits(visits)

    return f"""
    <h1>Current time in Moscow: {current_time}</h1>
    <p>Page visits: {visits}</p>
    """


@app.route("/visits")
def visits():
    return f"Total visits: {get_visits()}"


# Starting the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
