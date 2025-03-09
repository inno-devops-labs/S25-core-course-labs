from flask import Flask
from datetime import datetime
import pytz
import logging
from pythonjsonlogger import jsonlogger
import os


app = Flask(__name__)


log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
log_handler.setFormatter(formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


visits_file_path = '/data/visits.txt'


if not os.path.exists(visits_file_path):
    with open(visits_file_path, 'w') as f:
        f.write('0')


@app.route("/")
def home():
    try:
        with open(visits_file_path, 'r+') as f:
            content = f.read().strip()  # Читаем содержимое и удаляем пробелы
            if content.isdigit():  # Проверяем, что содержимое — это число
                visits = int(content)
            else:
                visits = 0  # Если файл пустой или содержит некорректные данные, начинаем с 0
            visits += 1
            f.seek(0)
            f.write(str(visits))
            f.truncate()
    except FileNotFoundError:
        # Если файл не существует, создаем его и начинаем с 1
        with open(visits_file_path, 'w') as f:
            visits = 1
            f.write(str(visits))

    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Current time in Moscow: {current_time}")
    return f"<h1>Current Time in Moscow: {current_time}</h1>"


@app.route("/visits")
def show_visits():
    with open(visits_file_path, 'r') as f:
        visits = f.read()
    return f"<h1>Total visits: {visits}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
