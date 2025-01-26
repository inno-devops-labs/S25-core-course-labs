from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def index():
    tz_msk = pytz.timezone('Europe/Moscow')
    current_time_msk = datetime.now(tz_msk)

    formatted_time = current_time_msk.strftime('%Y-%m-%d %H:%M:%S')

    return f'<h1>Current time in Moscow (MSK): {formatted_time}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
