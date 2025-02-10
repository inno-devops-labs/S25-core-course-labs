from flask import Flask
from datetime import datetime
import pytz


# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL ("/")
@app.route("/")
def moscow_time():
    """
    Handles requests to the root URL. Retrieves and displays the
    current time in the Moscow timezone.
    """

    # Set the timezone to Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')

    # Get the current date and time in the Moscow timezone
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    # Return the current time as an HTML response
    return f"<h1>Current Moscow Time: {current_time}</h1>"


# Run the Flask development server if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
