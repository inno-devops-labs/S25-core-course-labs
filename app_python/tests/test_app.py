import pytest
from datetime import datetime
import pytz
import time
import re
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Current time in Moscow:" in response.data


def test_time(client):
    response = client.get("/")
    assert response.status_code == 200

    true_moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    app_moscow_time = response.data.decode("utf-8").strip().split(": ", 1)[-1]

    assert re.match(
        r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", app_moscow_time
    ), f"Invalid format: {app_moscow_time}"

    time_difference = abs(
        (
            datetime.strptime(app_moscow_time, "%Y-%m-%d %H:%M:%S")
            - datetime.strptime(true_moscow_time, "%Y-%m-%d %H:%M:%S")
        ).total_seconds()
    )

    assert (
        time_difference <= 5
    ), f"Time difference too large: {time_difference} seconds"


def test_time_updates(client):
    response1 = client.get("/")
    assert response1.status_code == 200
    time1 = response1.data.decode("utf-8").strip().split(": ", 1)[-1]

    time.sleep(2)

    response2 = client.get("/")
    assert response2.status_code == 200
    time2 = response2.data.decode("utf-8").strip().split(": ", 1)[-1]

    assert time1 != time2, f"Time did not update: {time1} == {time2}"
