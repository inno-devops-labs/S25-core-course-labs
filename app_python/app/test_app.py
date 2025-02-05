import pytest
import pytz
from datetime import datetime
from fastapi.testclient import TestClient
from app.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_moscow_time_format(client):
    """Ensure response contains valid Moscow time format (without exact match)."""
    response = client.get("/")
    assert response.status_code == 200

    # Extract Moscow timezone time without exact seconds matching
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M")

    assert current_time in response.text  # Check only year-month-day hour-minute


def test_404_error(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
    assert "text/html" in response.headers["content-type"]
