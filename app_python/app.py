from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


def get_moscow_time():
    """Fetches the current time in Moscow timezone."""
    moscow_tz = pytz.timezone('Europe/Moscow')
    return datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def home():
    """Renders the main page displaying Moscow time."""
    current_time = get_moscow_time()
    return render_template('index.html', time=current_time)


if __name__ == '__main__':
    app.run()
