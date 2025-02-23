from flask import Flask
from datetime import datetime
import pytz
import logging
import json
from pythonjsonlogger import jsonlogger


app = Flask(__name__)


log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
log_handler.setFormatter(formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
def home():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Current time in Moscow: {current_time}")
    return f"<h1>Current Time in Moscow: {current_time}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
