from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_display_time_valid_zone():
    response = client.get("/current-time/moscow")
    assert response.status_code == 200
    assert "Current Time in" in response.text
