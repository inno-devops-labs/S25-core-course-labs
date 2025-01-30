from flask import Flask, render_template
from datetime import datetime
import pytz
import logging

# Initialize app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)


@app.route('/')
def home():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    # Log the time being returned
    app.logger.info(f'Returning time: {moscow_time}')

    return render_template('index.html', time=moscow_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
