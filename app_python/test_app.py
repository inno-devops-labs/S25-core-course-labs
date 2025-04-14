from fastapi.testclient import TestClient
from datetime import datetime
import pytz
from app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "current_time" in response.json()

def test_time_format():
    response = client.get("/")
    time_str = response.json()["current_time"]
    # Verify the time string format
    try:
        datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        assert True
    except ValueError:
        assert False, "Time format is incorrect"

def test_timezone():
    response = client.get("/")
    time_str = response.json()["current_time"]
    # Get current Moscow time
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
    # Get the response time
    response_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    # Compare hours (allowing small time difference due to execution time)
    assert abs(moscow_time.hour - response_time.hour) <= 1 