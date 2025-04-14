"""
Module containing time utils for the web application.
"""

from datetime import datetime
import pytz


def get_time():
    """Returns current time in Moscow."""
    return datetime.now(pytz.timezone("Europe/Moscow"))
