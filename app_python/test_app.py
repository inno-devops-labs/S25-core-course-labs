from fastapi.testclient import TestClient
from main import app, disable_visits
import main

import pytz
from datetime import datetime

client = TestClient(app)
disable_visits()


def get_time():
    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone)
    return time


def test_get():
    print(f'{main.with_visits}')
    disable_visits()
    print(f'{main.with_visits}')
    response = client.get("/")
    assert response.status_code == 200

    assert "moscow_time" in response.json()
    assert response.json()["moscow_time"] is not None

    response_time = datetime.fromisoformat(response.json()["moscow_time"])
    current_time = get_time()

    time_diff = abs(current_time - response_time).total_seconds()
    # allow 2 sec difference cause of execution delay
    assert time_diff < 2
