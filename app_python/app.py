from flask import Flask, render_template

from services.get_time_service import GetTimeService

from config import config

app = Flask(__name__)
app.config.from_mapping(config)


@app.get("/")
def get_time():
    """
    Shows the time in the timezone specified in the configuration file.
    """
    try:
        # Fetch the current time using the service
        current_time = GetTimeService.get_time_by_timezone(
            app.config["TIMEZONE_NAME"]
            )
        # Render the template with the fetched time
        return render_template("current_time.html", current_time=current_time)
    except ValueError as e:
        # Handle invalid timezone errors gracefully
        return f"Error: {e}", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
