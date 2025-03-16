from datetime import datetime
from flask import Flask, Response
from pytz import timezone
import os

VISITS_FILE = "visits"

def read_visits():
    """Read the number of visits from the file."""
    if os.path.isdir(VISITS_FILE):  # Check if 'visits' is mistakenly a directory
        print("Error: 'visits' is a directory! Deleting and creating a file.")
        os.rmdir(VISITS_FILE)  # Remove the directory
        open(VISITS_FILE, "w").close()  # Create an empty file
    
    try:
        with open(VISITS_FILE, "r", encoding="utf-8") as file:
            return int(file.read().strip() or 0)
    except (FileNotFoundError, ValueError):
        return 0

def write_visits(count):
    """Write the number of visits to the file."""
    with open(VISITS_FILE, "w", encoding="utf-8") as file:
        file.write(str(count))

def create_app():
    """
    Create and configure the Flask app.
    Returns:
        Flask app instance.
    """
    app = Flask(__name__)

    @app.route('/')
    def show_moscow_time():
        """
        Function to display the current time in Moscow timezone.
        Returns:
            Rendered HTML string with the current time in Moscow.
        """
        # Increment visit counter
        visits = read_visits() + 1
        write_visits(visits)

        # Get the current time in the Moscow timezone
        moscow_tz = timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

        # Return the HTML directly as a string
        return f'''
            <html>
                <head><title>Current Time in Moscow</title></head>
                <body>
                    <h1>Current time in Moscow: {current_time}</h1>
                    <p>Total Visits: {visits}</p>
                    <p><a href="/visits">See Visit Count</a></p>
                </body>
            </html>
        '''

    @app.route('/visits')
    def visit_count():
        """Display the number of visits recorded."""
        visits = read_visits()
        return f'''
            <html>
                <head><title>Visit Count</title></head>
                <body>
                    <h1>Total Visits: {visits}</h1>
                    <p><a href="/">Back to Time</a></p>
                </body>
            </html>
        '''

    return app

# Run the application only if executed directly
if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=5000, debug=True)

