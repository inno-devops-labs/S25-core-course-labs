from fastapi.testclient import TestClient
from datetime import datetime
import pytz
from main import app

client = TestClient(app)


def test_get_moscow_time():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "current_time_in_moscow" in data
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time_in_moscow = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    assert abs((datetime.strptime(data["current_time_in_moscow"], '%Y-%m-%d %H:%M:%S') -
                datetime.strptime(current_time_in_moscow, '%Y-%m-%d %H:%M:%S')).total_seconds()) < 5


def test_response_format():
    response = client.get("/")
    data = response.json()
    assert len(data) == 1
    assert isinstance(data["current_time_in_moscow"], str)
    try:
        datetime.strptime(data["current_time_in_moscow"], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        assert False, "The returned time is not in the expected format ('%Y-%m-%d %H:%M:%S')"