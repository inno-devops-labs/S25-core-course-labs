import pytest
import re
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_moscow_time(client):
    response = client.get("/")
    assert response.status_code == 200

    data = response.get_json()
    assert "timezone" in data
    assert "current_time" in data

    assert data["timezone"] == "Europe/Moscow"

    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    assert re.fullmatch(pattern, data["current_time"])
