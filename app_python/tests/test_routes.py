import re
from datetime import datetime, timedelta

import pytz
from fastapi import status
from fastapi.testclient import TestClient

from src.config import settings
from src.main import app

client = TestClient(app)

# Allowed tolerance for datetime in HTML in seconds
TIME_TOLERANCE_SECS: int = 2
# Pattern for datetime in format: DD/MM/YYYY HH:MM:SS
TIME_PATTERN: str = r"(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})"


def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "text/html; charset=utf-8"

    assert f"Current time in {settings.TIMEZONE}" in response.text

    upper_time = datetime.now(pytz.timezone(settings.TIMEZONE))
    lower_time = upper_time - timedelta(seconds=TIME_TOLERANCE_SECS)

    match = re.search(TIME_PATTERN, response.text)
    assert match is not None

    resp_time_str = match.group(1)
    resp_time = datetime.strptime(resp_time_str, settings.DATETIME_FORMAT)
    resp_time = pytz.timezone(settings.TIMEZONE).localize(resp_time)
    assert lower_time <= resp_time <= upper_time
