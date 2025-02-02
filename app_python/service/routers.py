"""
 In this module we implement routers for simplistic web service
 that provides current time in Moscow.

 SPDX-LICENCE: no-licence
 Author: Elon Max
"""

from datetime import datetime, timedelta, timezone

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from service import templates

TIMEZONE = "Europe/Moscow"

time_router = APIRouter()


@time_router.get("/", response_class=HTMLResponse)
async def serve_time() -> HTMLResponse:
    """
        Returns current time in Moscow
    """

    # get time in moscow tz
    zone = timezone(timedelta(hours=3))
    time = datetime                         \
        .now(timezone.utc)                  \
        .astimezone(zone)                   \
        .strftime("%Y-%m-%d %H:%M:%S %Z")

    # serve the page
    return HTMLResponse(
        content=templates.create_time_page(TIMEZONE, time),
        status_code=200)
