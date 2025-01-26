from datetime import datetime

import pytz
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    # Getting Moscow time
    msk_time = get_moscow_time()
    return render_template('home_page.html', time=msk_time)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


def get_moscow_time():
    return datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d-%m-%Y %H:%M:%S')
