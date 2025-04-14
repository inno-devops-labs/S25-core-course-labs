import pytest
from datetime import datetime
from unittest.mock import patch
from app import app
from app import TimeProvider
from fastapi.testclient import TestClient


@pytest.fixture
def mock_time_provider():
    with patch(
        "app.time_provider.get_current_time",
        return_value=datetime(2025, 1, 30, 10, 0, 0),
    ):
        yield


@pytest.fixture
def client():
    return TestClient(app)


def test_get_msc_time_endpoint(client, mock_time_provider):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"time": "2025-01-30 10:00:00"}


def test_get_msc_time_with_user_agent_htmlresponse(client, mock_time_provider):
    response = client.get("/", headers={"user-agent": "Mozilla/5.0"})
    assert response.status_code == 200
    assert "2025-01-30 10:00:00" in response.text and "Time in Moscow" in response.text


def test_get_msc_time_with_user_agent_jsonresponse(client, mock_time_provider):
    response = client.get("/", headers={"user-agent": "Not a browser"})
    assert response.status_code == 200
    assert response.json() == {"time": "2025-01-30 10:00:00"}


def test_get_msc_time_with_missing_user_agent(client, mock_time_provider):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"time": "2025-01-30 10:00:00"}


def test_get_msc_time_with_invalid_request_method(client):
    response = client.post("/")
    assert response.status_code == 405


def test_get_msc_time_with_invalid_request_path(client):
    response = client.get("/invalid-path")
    assert response.status_code == 404


def test_time_provider_get_current_time():
    time_provider = TimeProvider()
    current_time = time_provider.get_current_time("Europe/Moscow")
    assert isinstance(current_time, datetime)


def test_time_provider_get_current_time_invalid_timezone():
    time_provider = TimeProvider()
    with pytest.raises(Exception):
        time_provider.get_current_time("Invalid/Timezone")


def test_time_provider_get_current_time_different_timezones():
    time_provider = TimeProvider()
    moscow_time = time_provider.get_current_time("Europe/Moscow")
    new_york_time = time_provider.get_current_time("America/New_York")
    assert moscow_time != new_york_time
