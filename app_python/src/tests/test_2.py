"""
Test 2 for the web application.

- `test_read_time_json`: tests the current time in Moscow in JSON format
"""

from datetime import datetime
from fastapi.testclient import TestClient
from src.main import app
from src.utils import get_time


client = TestClient(app)


def test_read_time_json():
    """Tests the current time in Moscow in JSON format."""
    response = client.get("/time")
    assert response.status_code == 200
    response_data = response.json()
    current_time = get_time()
    assert datetime.fromisoformat(response_data["time"]).strftime(
        "%d.%m.%Y %H:%M:%S"
    ) == current_time.strftime("%d.%m.%Y %H:%M:%S")
