from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)


def get_moscow_time():
    """
    Get the current time in Moscow timezone.

    Returns:
        str: The current time in Moscow formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    try:
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
        return moscow_time
    except Exception as e:
        # Log error and return fallback message
        print(f"Error fetching Moscow time: {e}")
        return "Error fetching Moscow time"


@app.route('/')
def home():
    """
    Homepage route that returns the current Moscow time.

    Returns:
        str: HTML content displaying the Moscow time.
    """
    moscow_time = get_moscow_time()
    return f"<h1>Current time in Moscow: {moscow_time}</h1>"


@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.

    Args:
        error (Exception): The error object.

    Returns:
        str: Error message with HTTP 404 status code.
    """
    return "<h1>404 - Page Not Found</h1><p>The requested URL was not found on the server.</p>", 404


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True, host='0.0.0.0', port=5001)
