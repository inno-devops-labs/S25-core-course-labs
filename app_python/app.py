from flask import Flask
from datetime import datetime

import pytz


app = Flask(__name__)

def get_page_text(cur_time, city="Moscow"):
    return f"""
        <h3>This is an application for the DevOps core course</h3>
        <h1>The current time in {city} is:</h1>
        <h1>{cur_time}</h1>
    """


@app.route('/')
def home():
    time_zone = pytz.timezone("Europe/Moscow")
    cur_time = datetime.now(time_zone).strftime('%d/%m/%Y %H:%M:%S')

    return get_page_text(cur_time=cur_time)


if __name__ == '__main__':
    app.run(debug=True)
