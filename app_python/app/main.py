from fastapi import FastAPI
from datetime import datetime
from prometheus_fastapi_instrumentator import Instrumentator
import pytz
from pathlib import Path
import os

app = FastAPI()

VISITS_FILE = Path("/data/visits.txt")

os.makedirs(VISITS_FILE.parent, exist_ok=True)
if not VISITS_FILE.exists():
    VISITS_FILE.write_text("0")

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)


@app.get("/time")
async def get_moscow_time():
    current_visits = int(VISITS_FILE.read_text())
    VISITS_FILE.write_text(str(current_visits + 1))

    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"moscow_time": time}


@app.get("/visits")
async def get_visits():
    visits = VISITS_FILE.read_text()
    return {"visits": visits}