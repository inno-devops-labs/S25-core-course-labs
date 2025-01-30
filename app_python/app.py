from flask import Flask, render_template
import ntplib
import datetime
import logging

# NTP server to use for getting current time
NTP_SERVER = '0.ru.pool.ntp.org'

# Name for log file
LOG_FILENAME = 'app.log'

# Create new logger
logger = logging.getLogger('msk-time')
# Write logs to log file
file_handler = logging.FileHandler(LOG_FILENAME)
# Use custom formatter
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

"""Return the current time by making NTP request"""
def get_date() -> datetime.datetime:
    # Initialize NTP client
    c = ntplib.NTPClient()

    # Make NTP request to NTP_SERVER
    response = c.request(NTP_SERVER)
    
    # Turn timestamp into datetime object
    date = datetime.datetime.fromtimestamp(response.tx_time)

    return date

"""Return the datetime formatted as HH:MM:SS"""
def format_time(date: datetime.datetime) -> str:
    formatted_time = f'{date.hour:02}:{date.minute:02}:{date.second:02}'
    return formatted_time

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Get current time
        date = get_date()

        # Get time in HH::MM:SS format
        formatted_time = format_time(date)
        return render_template('index.html', time=formatted_time)
    except Exception as e:
        # If an exception occurs, log it with callstack
        logger.error(e.__class__.__name__, exc_info=True)

        # Return Internal Error page
        return render_template('error.html'), 500

if __name__ == '__main__':
    app.run()
