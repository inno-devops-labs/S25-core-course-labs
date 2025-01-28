from flask import Flask, render_template
from datetime import datetime
from pytz import timezone

TIMEZONE = 'Europe/Moscow'

app = Flask(__name__)


def get_current_time(zone: str) -> str:
    return datetime.now(timezone(zone)).strftime('%d-%m-%Y %H:%M:%S')


@app.route('/')
def time_page():
    return render_template(
        'time.html',
        time=get_current_time(TIMEZONE),
        timezone=TIMEZONE,
    )


if __name__ == '__main__':
    app.run()
