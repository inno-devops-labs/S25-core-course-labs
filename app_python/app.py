from flask import Flask
from datetime import datetime
import pytz
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

app = Flask(__name__)


@app.route('/')
def show_moscow_time():
    time_zone = pytz.timezone('Europe/Moscow')
    time = datetime.now(time_zone).strftime('%Y-%m-%d %H:%M:%S')
    app.logger.info(f"User requested time, current Moscow Time: {time}")
    return f"<h1>Moscow time : {time}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
