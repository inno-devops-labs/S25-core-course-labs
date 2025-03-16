import os
import logging
import sys
from flask import Flask, jsonify, render_template, request, Response
from datetime import datetime
import pytz
import requests
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest, Counter, Histogram

# Инициализация приложения Flask
app = Flask(__name__)

# Константы
VISITS_FILE = "/app/data/visits"
TIME_API_URL = "https://www.timeapi.io/api/time/current/zone?timeZone=Europe%2FMoscow"
moscow_tz = pytz.timezone('Europe/Moscow')

# Настройка логирования
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Настройка метрик Prometheus
REQUESTS_COUNTER = Counter('requests_total', 'Total number of requests')
VISIT_COUNTER = Counter('visits_total', 'Total number of visits')


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
        app.logger.error(f"Error during API request: {e}")
        return None


@app.before_request
def log_request_info():
    app.logger.info("Received request: %s %s from %s", request.method, request.url, request.remote_addr)


@app.route('/')
def index():
    # Увеличиваем счетчик посещений
    count = 0
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as f:
            count = int(f.read())

    count += 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))

    VISIT_COUNTER.inc()  # Увеличиваем счетчик посещений для Prometheus

    # Получаем текущее время из API или локально
    time_from_api = get_time_from_api()
    if time_from_api:
        current_time = time_from_api
    else:
        current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')

    # Рендерим шаблон с текущим временем
    return render_template('index.html', current_time=current_time, visits=count)


@app.route('/time')
def get_time():
    time_from_api = get_time_from_api()

    if time_from_api:
        return jsonify({'time': time_from_api, 'status': 'success'})
    else:
        moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
        return jsonify({'time': moscow_time, 'status': 'error'})


@app.route('/visits')
def visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as f:
            return f"Visits: {f.read()}"
    else:
        return "No visits recorded yet."


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)