from flask import Flask, jsonify, render_template
from datetime import datetime
import pytz
import requests

app = Flask(__name__)

moscow_tz = pytz.timezone('Europe/Moscow')

TIME_API_URL = "https://www.timeapi.io/api/time/current/zone?timeZone=Europe%2FMoscow"


def get_time_from_api():
    try:
        response = requests.get(TIME_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get('dateTime'):
            time = data['dateTime'][11:19]
            return time
        return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def get_time():
    time_from_api = get_time_from_api()

    if time_from_api:
        return jsonify({'time': time_from_api, 'status': 'success'})
    else:
        moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
        return jsonify({'time': moscow_time, 'status': 'error'})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
