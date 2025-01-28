from datetime import datetime

import pytz
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Gets the moscow time and displays it in the rendered html page
    """

    msk_time = get_moscow_time()
    return render_template('home_page.html', time=msk_time)


@app.errorhandler(404)
def not_found(error):
    """
    Shows custom error page for 404 (not found) error
    """
    return render_template('404.html')


def get_moscow_time():
    """
    Gets moscow time and returns it in the string format.
    Example: 28-01-2025 23:30:17
    """
    return datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d-%m-%Y %H:%M:%S')
