import pytest
from lab1 import app
from routes import get_time
import pytz
from datetime import datetime
import re
import time


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_homepage_status(client):
    # checking that the main page is available
    response = client.get('/')
    assert response.status_code == 200


def test_homepage_contains_time(client):
    # check that the main page contains the correct time.
    response = client.get('/')
    html = response.get_data(as_text=True)
    match = re.search(r'\d{2}:\d{2}:\d{2}', html)
    assert match, "time not found"
    current_time = get_time()
    assert match.group(
        0) == current_time, f"Expected {current_time},found {match.group(0)}"


def test_get_time_format():
    # Check that get_time() returns a string in the correct format
    time_str = get_time()
    assert re.match(r'^\d{2}:\d{2}:\d{2}$',
                    time_str), f"Incorrect format {time_str}"


def test_get_time_correctness():
    # Check that get_time() return current Moscow time
    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
    actual_time = get_time()
    assert abs(datetime.strptime(actual_time, "%H:%M:%S") - datetime.strptime(
        expected_time, "%H:%M:%S")).seconds <= 1, \
        f"Expected {expected_time}, but found {actual_time}"


def test_get_time_multiple_calls():
    # Check that get_time() it works correctly for consecutive calls
    times = []
    for _ in range(5):
        actual_time = get_time()
        times.append(actual_time)
        time.sleep(0.5)

    assert all(times), "Some calls get_time() return empty values"
    assert len(
        set(times)) > 1, "The time does not change for consecutive calls"


def test_get_time_different_timezones(monkeypatch):
    # Checking that the TIMEZONE change in affects the result
    ny_tz = pytz.timezone("Asia/Tokyo")
    expected_time = datetime.now(ny_tz).strftime("%H:%M:%S")
    actual_time = get_time("Asia/Tokyo")

    assert abs(datetime.strptime(actual_time, "%H:%M:%S") - datetime.strptime(
        expected_time, "%H:%M:%S")).seconds <= 1, \
        f"Expected {expected_time}, but found {actual_time}"
