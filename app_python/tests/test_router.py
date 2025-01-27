from fastapi.testclient import TestClient
from datetime import datetime
import pytz

from app_python.app import app

client = TestClient(app)


def test_get_moscow_time():
    response = client.get("/msc_time")
    assert response.status_code == 200

    data = response.json()

    assert "current_time_in_moscow" in data

    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_format = "%Y-%m-%d %H:%M:%S"

    try:
        returned_time_naive = datetime.strptime(data["current_time_in_moscow"], expected_format)
        returned_time = moscow_tz.localize(returned_time_naive)
    except ValueError:
        assert False, "Time format is invalid"

    moscow_time = datetime.now(tz=moscow_tz)

    delta = abs((moscow_time - returned_time).total_seconds())
    assert delta < 5, f"Time delta too large: {delta} seconds"