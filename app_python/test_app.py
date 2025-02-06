import pytest
from app import app
import re


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_moscow_time(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Current Time in Moscow:" in response.data.decode()

    # Проверяем формат времени YYYY-MM-DD HH:MM:SS
    time_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    assert re.search(time_pattern, response.data.decode())
