"""
 In this module we implement routers for simplistic web service
 that provides current time in Moscow.

 SPDX-LICENCE: no-licence
 Author: Elon Max
"""

from datetime import datetime, timedelta, timezone
import os

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from service import templates

TIMEZONE = "Europe/Moscow"
VISITS_FILE = "/data/visits.txt"

time_router = APIRouter()


def get_visits_count() -> int:
    """Reads the visits count from a file."""
    if not os.path.exists(VISITS_FILE):
        return 0
    with open(VISITS_FILE, "r", encoding="utf-8") as file:
        try:
            return int(file.read().strip())
        except ValueError:
            return 0


def increment_visits() -> int:
    """Increments visit count and stores it into a file."""
    count = get_visits_count() + 1
    with open(VISITS_FILE, "w", encoding="utf-8") as file:
        file.write(str(count))
    return count


@time_router.get("/", response_class=HTMLResponse)
async def serve_time() -> HTMLResponse:
    """
    Returns current time in Moscow.
    """
    # get time in moscow tz
    zone = timezone(timedelta(hours=3))
    time = datetime                         \
        .now(timezone.utc)                  \
        .astimezone(zone)                   \
        .strftime("%Y-%m-%d %H:%M:%S %Z")

    # increment visits
    increment_visits()

    # serve the page
    return HTMLResponse(
        content=templates.create_time_page(TIMEZONE, time),
        status_code=200
    )


@time_router.get("/visits", response_class=HTMLResponse)
async def visits() -> HTMLResponse:
    """
    Returns the number of times the main page was visited.
    """
    visits_count = get_visits_count()

    # serve the page
    return HTMLResponse(
        content=templates.create_visits_page(count=visits_count),
        status_code=200
    )
