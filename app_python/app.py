from flask import Flask, render_template
from datetime import datetime
from threading import Lock
from pytz import timezone

TIMEZONE = 'Europe/Moscow'

VISITS_FILE = 'visits/visits'

lock = Lock()

app = Flask(__name__)


def _write_visits(visits: int) -> None:
    with lock:
        with open(VISITS_FILE, 'w') as fp:
            fp.write(str(visits))


def _get_visits() -> int:
    try:
        with lock:
            with open(VISITS_FILE) as fp:
                return int(fp.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def increase_visits() -> None:
    visits = _get_visits()
    _write_visits(visits + 1)


def get_visits() -> int:
    return _get_visits()


def get_current_time(zone: str) -> str:
    return datetime.now(timezone(zone)).strftime('%d-%m-%Y %H:%M:%S')


@app.route('/')
def time_page():
    increase_visits()

    return render_template(
        'time.html',
        time=get_current_time(TIMEZONE),
        timezone=TIMEZONE,
    )


@app.route('/visits')
def visits_page():
    return str(get_visits())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
