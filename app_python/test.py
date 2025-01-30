from datetime import datetime
from unittest.mock import patch
import pytest
from app import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)

# json response
def test_get_msc_time(client):
    # mock current time
    with patch('app.time_provider.get_current_time', return_value=datetime(2025, 1, 30, 10, 0, 0)):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"time": "2025-01-30 10:00:00"}

# html response
def test_get_msc_time_with_user_agent(client):
    with patch('app.time_provider.get_current_time', return_value=datetime(2025, 1, 30, 10, 0, 0)):
        response = client.get("/", headers={"user-agent": "Mozilla/5.0"})
        assert response.status_code == 200
        assert "2025-01-30 10:00:00" in response.text
