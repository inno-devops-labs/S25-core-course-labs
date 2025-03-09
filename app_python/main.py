from fastapi import FastAPI
from datetime import datetime
import os
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

VISITS_FILE = "/app/data/visits.txt"

def get_visits_count():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "r") as file:
            count = file.read().strip()
            return int(count) if count.isdigit() else 0
    return 0

def save_visits_count(count):
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)  # Создаем директорию, если ее нет
    with open(VISITS_FILE, "w") as file:
        file.write(str(count))

@app.get("/")
async def get_moscow_time():
    moscow_timezone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"Moscow Time": moscow_time}

@app.get("/visits")
async def get_visits():
    count = get_visits_count() + 1  # Увеличиваем счетчик при каждом посещении
    save_visits_count(count)
    return {"Visits": count}
