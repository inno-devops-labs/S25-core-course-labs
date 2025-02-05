import sys
import time
from fastapi.testclient import TestClient
from datetime import datetime

import pytz

sys.path.append("src")

from main import app

client = TestClient(app)


def test_get_moscow_time():
    """Test that the endpoint returns a valid response (200 status code) with 'moscow_time' key."""
    response = client.get("/get_moscow_time")
    assert response.status_code == 200
    assert "moscow_time" in response.json()


def test_moscow_time_format():
    """Test that the returned correctly formated time value."""
    response = client.get("/get_moscow_time")
    moscow_time = response.json()["moscow_time"]
    try:
        datetime.strptime(moscow_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        assert False, f"Time format is incorrect: {moscow_time}"


def test_moscow_time_updates():
    """Test that the Moscow time updates between requests."""
    response1 = client.get("/get_moscow_time")
    time1 = response1.json()["moscow_time"]

    time.sleep(1)

    response2 = client.get("/get_moscow_time")
    time2 = response2.json()["moscow_time"]

    assert time1 != time2, "Time did not update between requests"


def test_moscow_time_timezone():
    """Test that the returned time is in the correct timezone (Europe/Moscow)."""
    response = client.get("/get_moscow_time")
    moscow_time_str = response.json()["moscow_time"]

    moscow_time = datetime.strptime(moscow_time_str, "%Y-%m-%d %H:%M:%S")

    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = moscow_tz.localize(moscow_time)

    utc_now = datetime.now(pytz.utc)
    expected_moscow_time = utc_now.astimezone(moscow_tz)

    time_difference = abs((expected_moscow_time - moscow_time).total_seconds())
    assert (
        time_difference <= 1
    ), f"Returned time is not in the correct timezone: {moscow_time_str}"
