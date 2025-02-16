from datetime import datetime, timezone, timedelta
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="resources/templates",
    static_folder="resources/static"
)

# Moscow time zone is UTC+3
TIMEZONE = 3
DATE_FORMAT = "%a %b %d %H:%M:%S %Y"

# The main page serves time in Moscow
@app.route("/")
def serve_time():
    # Get time in the required timezone and format it
    time_moscow = datetime.now(timezone(timedelta(hours=TIMEZONE)))
    time_moscow = time_moscow.strftime(DATE_FORMAT)

    # Render the template and send it to user
    return render_template("template.html", time_msk=time_moscow)
