import logging
import os
from datetime import datetime
from logging import FileHandler

import pytz
from flask import current_app as app, render_template, jsonify

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
    get_and_increment_visits()

    return render_template('index.html', moscow_time=moscow_time)


@app.route('/visits', methods=['GET'])
def visits():
    """
    :return: JSON response with the visits count from the `visits` file
    """
    count = get_and_increment_visits(need_increment=False)
    app.logger.info("Accessed /visits endpoint. Current count: %d", count)
    return jsonify({'visits': count})


def get_and_increment_visits(need_increment: bool = True):
    """
    Read counter from file
    :return: updated visits count as an integer.
    """
    folder = 'data'

    if not os.path.exists(folder):
        os.makedirs(folder)

    visits_file = os.path.join(folder, 'visits')

    count = 0
    if os.path.exists(visits_file):
        try:
            with open(visits_file, 'r') as f:
                data = f.read().strip()
                if data.isdigit():
                    count = int(data)
                else:
                    count = 0
        except Exception as e:
            app.logger.error("Error reading visits file: %s", e)
            count = 0

    if need_increment:
        count += 1

    try:
        with open(visits_file, 'w') as f:
            f.write(str(count))
    except Exception as e:
        app.logger.error("Error writing visits file: %s", e)

    return count
