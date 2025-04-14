from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")

def get_time():
   
    # Указываем часовой пояс Москвы
    moscow_tz = pytz.timezone('Europe/Moscow')

    # Получаем текущее время в Москве
    moscow_time = datetime.now(moscow_tz)

    # Форматируем время
    time = moscow_time.strftime("%H:%M:%S")
    return render_template('index.html', current_time = time)

if __name__ == "__main__":
    app.run(host="0.0.0.0")