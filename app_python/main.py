from fastapi import FastAPI
import os
from datetime import datetime
import pytz
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

VISITS_FILE = "/app/data/visits.txt"
with_visits = True
app = FastAPI()


def initialize_visits_file():
    print(f'visits {with_visits}')
    if with_visits:
        os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
        if not os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, "w") as f:
                f.write("0")


def disable_visits():
    global with_visits
    with_visits = False


def get_visits():
    if with_visits:
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, "r") as f:
                return int(f.read().strip())
    return 0


def increment_visits():
    visits = get_visits() + 1
    with open(VISITS_FILE, "w") as f:
        f.write(str(visits))
    return visits


@app.get("/")
def get_time():
    if with_visits:
        initialize_visits_file()
        increment_visits()
    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone)
    return {"moscow_time": time.isoformat()}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/visits")
def get_visits_count():
    return {"visits": get_visits()}
