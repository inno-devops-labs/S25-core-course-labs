import os
import logging
from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

VISITS_FILE = "/app/visits/visits.txt"  # Используем путь, соответствующий volume

@app.route("/")
def current_time():
    """
    Function to display the current time in Moscow
    """
    tz_moscow = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(tz_moscow).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Served current time: {moscow_time}")
    return render_template("index.html", time=moscow_time)

@app.route("/visits")
def visit_counter():
    """
    Function to count and display visits
    """
    try:
        if not os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, "w") as f:
                f.write("0")

        with open(VISITS_FILE, "r+") as f:
            count = int(f.read().strip() or 0)  # Читаем текущее значение
            count += 1  # Увеличиваем счетчик
            f.seek(0)  # Перемещаем курсор в начало файла
            f.write(str(count))  # Записываем новое значение
            f.truncate()  # Очищаем остаток файла

        return f"Visit count: {count}"

    except Exception as e:
        logging.error(f"Error processing /visits: {str(e)}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
