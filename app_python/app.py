"""Bottle web application that shows the current time and date in Moscow.
Author: Evgeny B.
"""

from datetime import datetime, timedelta, timezone

from bottle import Bottle, response, run

# Create a Bottle app instance
app = Bottle()

# Define the MSK timezone (UTC+3)
MSK_TIMEZONE = timezone(timedelta(hours=3))


@app.route("/")
def show_time():
    """Show the current time and date in Moscow."""
    # Get the current time in Moscow
    now = datetime.now(MSK_TIMEZONE)
    formatted_time = now.strftime("%H:%M:%S")
    formatted_date = now.strftime("%d.%m.%Y")

    # Set the response content type to HTML
    response.content_type = "text/html; charset=utf-8"
    return (
        f"<html><body><h1>Current time and date in Moscow</h1>"
        f"<p>Time: {formatted_time}</p>"
        f"<p>Date: {formatted_date}</p></body></html>"
    )


# Run the Bottle app
if __name__ == "__main__":
    # Run the Bottle app on the server
    run(app, host="0.0.0.0", port=8080, debug=False, reloader=False)
