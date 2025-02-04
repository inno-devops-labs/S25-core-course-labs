from datetime import datetime

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_moscow_time():
    """
    Tests / endpoint, which sends Moscow time.
    """
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert "moscow_time" in data

    moscow_time = data["moscow_time"]
    try:
        datetime.strptime(moscow_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        assert False, f"Invalid time format: {moscow_time}"

    print(f"Test was passed! Moscow time: {moscow_time}")


def test_invalid_endpoint():
    """
    Tests invalid endpoint.
    """
    response = client.get("/invalid")
    assert response.status_code == 404
