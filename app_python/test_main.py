from datetime import datetime, time

import pytz
from fastapi.testclient import TestClient

from main import app, TIME_FORMAT, TIMEZONE

client = TestClient(app)

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

MAX_DIFF = 1


def test_get_current_time():
    response = client.get("/api/time")

    assert response.status_code == 200, "The response status code is not 200"
    assert (
        response.headers["content-type"] == "application/json"
    ), "The response content type is not JSON"

    data = response.json()

    assert "time" in data, "The response does not contain the 'time' field"

    time_str = data["time"]

    assert isinstance(time_str, str), "The 'time' field is not a string"

    try:
        parsed_time = datetime.strptime(time_str, TIME_FORMAT).time()
    except ValueError:
        assert False, "The 'time' field is not in the correct format"

    current_time = datetime.now(pytz.timezone(TIMEZONE)).time()

    def get_seconds(t: time) -> int:
        seconds_in_hour = t.hour * SECONDS_IN_HOUR
        seconds_in_minute = t.minute * SECONDS_IN_MINUTE

        return seconds_in_hour + seconds_in_minute + t.second

    diff = abs(get_seconds(current_time) - get_seconds(parsed_time))

    assert diff <= MAX_DIFF, "The time difference is too big"


def test_get_current_time_html():
    response = client.get("/")

    assert response.status_code == 200, "The response status code is not 200"
    assert response.headers["content-type"].startswith(
        "text/html"
    ), "The response content type is not HTML"
