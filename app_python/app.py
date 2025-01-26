from flask import Flask, render_template
from datetime import datetime

import pytz


app = Flask(__name__)

# global vars that represent a city to display time in
CITY = "Moscow"
TIMEZONE = "Europe/Moscow"


# function for returning date and time in the given timezone
def get_current_time(str_timezone):
    try:
        tz = pytz.timezone(str_timezone)
        return datetime.now(tz).strftime('%d/%m/%Y %H:%M:%S')
    except pytz.UnknownTimeZoneError:
        app.logger.error(f"Unknown time zone: {str_timezone}")
        return None


# rendering the home (main) page
@app.route('/')
def home():
    time_zone = get_current_time(TIMEZONE)
    if time_zone is None:
        return "Invalid given timezone", 400
    
    cur_time = datetime.now(time_zone).strftime('%d/%m/%Y %H:%M:%S')

    return render_template('home.html', cur_time=cur_time, city=CITY)


if __name__ == '__main__':
    app.run(debug=True)
