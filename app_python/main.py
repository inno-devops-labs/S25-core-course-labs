from flask import Flask
from datetime import datetime
import pytz
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/')
def current_time():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    time_str = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

    # Log the current time request
    logger.info(f"Current time requested: {time_str}")

    return f"Current time in Moscow: {time_str}"


if __name__ == '__main__':
    # Log when the server starts
    logger.info("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000)
