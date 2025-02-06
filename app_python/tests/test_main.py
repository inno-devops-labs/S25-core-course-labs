import time
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


def test_time_updates_on_reload():
    """
    Tests whether the time updates when the page is reloaded.
    """
    response1 = client.get("/")
    assert response1.status_code == 200
    data1 = response1.json()
    assert "moscow_time" in data1
    time1 = data1["moscow_time"]

    time.sleep(2)

    response2 = client.get("/")
    assert response2.status_code == 200
    data2 = response2.json()
    assert "moscow_time" in data2
    time2 = data2["moscow_time"]

    assert time1 != time2, "Time did not update on reload"

    print(f"Test was passed! Time updated from {time1} to {time2}")
