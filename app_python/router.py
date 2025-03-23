import pytz
import asyncio
import os
from datetime import datetime
from schemas import TimeSerializer
from fastapi import APIRouter

router = APIRouter(prefix="", tags=["Time"])

counter = 0
lock = asyncio.Lock()


def vistits_update(counter: int):
    if not os.path.exists('visits.txt'):
        f = open("visits.txt", "w")
        f.write(str(0))

    f = open("visits.txt", "r")
    if os.stat("visits.txt").st_size == 0:
        ex_count = 0
    else:
        ex_count = int(f.read())

    f = open("visits.txt", "w")
    f.write(str(counter + ex_count))
    f.close()


@router.get("/", summary="Main page")
async def main():
    global counter

    async with lock:
        counter += 1
    vistits_update(counter)
    counter = 0

    return {
        "message": "Hello, proceed to /time to see current MSK time or /visits"
        + " to check overall visits of main page and /time endpoint"
    }


@router.get("/time", summary="MSK time", response_model=TimeSerializer)
async def get_time():
    global counter

    async with lock:
        counter += 1
    vistits_update(counter)
    counter = 0

    tz = pytz.timezone('Europe/Moscow')
    return {"time": str(datetime.now(tz))}


@router.get("/visits", summary="Visits counter")
async def get_visits():

    f = open("visits.txt", "r")
    if os.stat("visits.txt").st_size == 0:
        count = 0
    else:
        count = int(f.read())

    return {"visits_count": str(count)}
