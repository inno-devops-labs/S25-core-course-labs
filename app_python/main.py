from fastapi import FastAPI
from datetime import datetime
import uvicorn
import pytz
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

VISITS_FILE = "data/visits"


def read_visits():
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")
    with open(VISITS_FILE, "r") as f:
        return int(f.read().strip())


def write_visits(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


@app.get("/")
def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    count = read_visits()
    count += 1
    write_visits(count)
    return {"current_time_in_moscow": current_time}


@app.get("/visits")
def get_visits():
    count = read_visits()
    return {"visits": count}


Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
