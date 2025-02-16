import pytest
from datetime import datetime
from unittest.mock import patch
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_route_status_code(client):
    print("\n=== Testing status code ===")
    response = client.get("/")
    assert response.status_code == 200


def test_home_route_time_display(client):
    # Test with mocked time
    test_time = datetime(2025, 1, 1, 12, 30, 0)
    with patch("app.datetime") as mock_datetime:
        mock_datetime.now.return_value = test_time
        response = client.get("/")
        assert b"2025-01-01 12:30:00" in response.data
