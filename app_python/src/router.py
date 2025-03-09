import datetime
import os

import pytz
from fastapi import APIRouter
from prometheus_client import generate_latest
from starlette.responses import PlainTextResponse

from src.schema import GetTimeResponse

router = APIRouter()

VISITS_FILE = "/data/visits.txt"


def increment_visit_counter():
    if not os.path.isfile(VISITS_FILE):
        with open(VISITS_FILE, "w") as file:
            file.write("0")
    with open(VISITS_FILE, "r") as file:
        v = int(file.read())
    with open(VISITS_FILE, "w") as file:
        file.write(str(v + 1))


@router.get("/msc_time")
async def get_moscow_time() -> GetTimeResponse:
    increment_visit_counter()
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.datetime.now(tz=moscow_tz)
    return GetTimeResponse(current_time=moscow_time.strftime("%Y-%m-%d %H:%M:%S"))


@router.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    return generate_latest()


@router.get("/visits")
async def get_visits():
    if not os.path.exists(VISITS_FILE):
        return {"visits": 0}
    with open(VISITS_FILE, 'r') as f:
        visits = int(f.read().strip())
    return {"visits": visits}
