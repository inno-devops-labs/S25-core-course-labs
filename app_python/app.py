from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)  # initialize the Flask application


@app.route("/")  # define the main page route
def index():
    # Set the time zone to Moscow
    moscow_tz = pytz.timezone("Europe/Moscow")
    # Get the current time in format HH:MM:SS
    current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
    # Render the html page, passing there the current time
    return render_template("index.html", time=current_time)


if __name__ == "__main__":
    # Run the application
    app.run(host="0.0.0.0", port=5000)
