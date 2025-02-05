import pytest
from app_python.app import app
from datetime import datetime
import pytz


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Current time in Moscow" in response.data


def test_moscow_time(client):
    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M")
    response = client.get("/")
    assert response.status_code == 200
    assert expected_time.encode() in response.data
