from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_display_time_invalid_zone():
    response = client.get("/current-time/invalid_zone")
    assert response.status_code == 200
    assert "Invalid time zone: invalid_zone" in response.text
