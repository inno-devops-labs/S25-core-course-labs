from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


def get_visits():
    try:
        with open('visits.txt', 'r') as file:
            visits = int(file.read())
        return visits
    except FileNotFoundError:
        with open('visits.txt', 'w') as file:
            file.write('0')
        return 0


def update_visits(visits):
    with open('visits.txt', 'w') as file:
        file.write(str(visits))


@app.route('/')
def index():
    tz_msk = pytz.timezone('Europe/Moscow')
    current_time_msk = datetime.now(tz_msk)

    formatted_time = current_time_msk.strftime('%Y-%m-%d %H:%M:%S')

    return f'<h1>Current time in Moscow (MSK): {formatted_time}</h1>'

@app.route('/visits')
def get_visits_route():
    try:
        visits = get_visits()
        return f'The number of visits is: {visits}'
    except Exception as e:
        return f'An error occurred: {str(e)}'


if __name__ == '__main__':
    app.run(debug=True)
