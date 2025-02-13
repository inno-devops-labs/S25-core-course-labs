import logging
from datetime import datetime
from logging import FileHandler

import pytz
from flask import current_app as app, render_template

file_handler = FileHandler('app.log')
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)


@app.route('/')
def index():
    """
    Main route with the single program functionality
    :return: the dedicated page
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')

    app.logger.info("Accessed / endpoint: %s", f"Moscow time is: {moscow_time}")

    return render_template('index.html', moscow_time=moscow_time)
