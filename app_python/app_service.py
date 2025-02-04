"""
functions for the app.(logic section).
"""

from datetime import datetime

import pytz
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app_python")


def get_time(request: Request, timezone: str = "Europe/Moscow") -> str:
    """
    Returns the current time in the given timezone.
    :param timezone: The timezone to get the current time from. (Optional, default: Europe/Moscow)
    :request: Request object essential for passing
      the necessary context (like session data or query parameters).
    """

    return templates.TemplateResponse(
        "time_template.html",
        {"request": request, "current_time": get_tz_time(timezone)},
    )


def get_tz_time(timezone) -> str:
    """
    Returns the current time in the given timezone.
    :param timezone: The timezone to get the current time from.
    """
    return datetime.now(pytz.timezone(timezone)).strftime("%H:%M (%I:%M %p)")
