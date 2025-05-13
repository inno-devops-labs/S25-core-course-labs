"""
Moscow Time 
Copyright (c) 2025 Artur Lukianov. Licensed under MIT License.

A Flask-based web application that displays the current time in Moscow, Russia with second precision. It is nice and cool. Exclusively for DevOps course.

See instllation and usage instructions in README.md

Features:
- Timezone-aware calculations using pytz
- Clean separation of concerns
- Production-ready configuration
- Comprehensive error handling
- Detailed documentation

Environment Requirements:
- Python 3.9+
- Flask 3.1.0
- pytz 2024.2
"""

from datetime import datetime
import logging
from typing import Tuple

from flask import Flask, render_template, Response
import pytz

# Configuration Constants
class Config:
    """Application configuration settings."""
    TIMEZONE = 'Europe/Moscow' # If in the future the timezone can be changed, better move it already
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    REFRESH_INTERVAL = 1  # seconds
    HOST = '0.0.0.0'
    PORT = 5000
    LOG_LEVEL = logging.INFO # Some logging never was bad

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Configure logging
logging.basicConfig(
    level=Config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_moscow_time() -> Tuple[str, str]:
    """
    Retrieve current Moscow time with error handling.
    
    Returns:
        tuple: (date_string, time_string) formatted strings
        
    Raises:
        pytz.exceptions.UnknownTimeZoneError: Invalid timezone configuration
    """
    try:
        utc_now = datetime.now(pytz.utc)
        moscow_tz = pytz.timezone(Config.TIMEZONE)
        moscow_now = utc_now.astimezone(moscow_tz)
        full_time = moscow_now.strftime(Config.DATE_FORMAT)
        return full_time.split(' ', 1)
    except pytz.exceptions.UnknownTimeZoneError as e:
        logger.error(f"Invalid timezone configuration: {Config.TIMEZONE}")
        raise e

@app.route('/', methods=['GET'])
def display_time() -> Response:
    """
    Handle main endpoint request.
    
    Returns:
        Response: Rendered HTML template with current time
        
    Error Handling:
        - Returns 500 status code on timezone errors
        - Logs errors with traceback information
    """
    try:
        date_str, time_str = get_moscow_time()
        logger.debug(f"Successfully retrieved time: {date_str} {time_str}")
        return render_template(
            'index.html',
            time=time_str,
            date=date_str,
            refresh=Config.REFRESH_INTERVAL
        )
    except Exception as e:
        logger.exception("Failed to retrieve Moscow time")
        return render_template(
            'error.html',
            error_message="Unable to retrieve current time"
        ), 500

if __name__ == '__main__':
    # Production note: Use WSGI server for deployment
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        # Never run with debug=True in production
        debug=(Config.LOG_LEVEL == logging.DEBUG)
    )
