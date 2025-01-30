import pytz
from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Global variable with timezone
TIME_ZONE = ""
CONFIG_FILE = "config.txt"


def get_timezone() -> str():
    """
    Loading timezone frome configuration file
    """
    try:
        with open(CONFIG_FILE, "r") as config_file:
            time_zone = config_file.read().strip()

        return time_zone if time_zone else "Europe/Moscow"
    except Exception:

        # Default value
        return "Europe/Moscow"


@app.route("/")
def current_time() -> str():
    """
    Returns the current time in timezone formatted as HH:MM:SS.
    """
    global TIME_ZONE

    # Set up TIME_ZONE if it was not
    if TIME_ZONE == "":
        time_zone = get_timezone()

        try:
            TIME_ZONE = pytz.timezone(time_zone)
        except Exception:
            TIME_ZONE = pytz.timezone("Europe/Moscow")

    time = datetime.now(TIME_ZONE)
    return f"Current time in {TIME_ZONE} is {time.strftime("%H:%M:%S")}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
