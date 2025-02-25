from app.utils.time_helper import get_moscow_time
from freezegun import freeze_time
from fastapi.testclient import TestClient
from app.main import app
import time

client = TestClient(app)


@freeze_time("2025-02-01 14:00:00")
def test_get_moscow_time_from_utc():
    """
    Test that the function returns the correct time in Moscow
    when provided with time in other timezone.
    """
    assert get_moscow_time() == "2025-02-01 17:00:00"


@freeze_time("2025-02-01 14:00:00")
def test_server_response():
    """
    Test that the server returns the correct response.
    """
    response = client.get("/")

    assert response.status_code == 200
    assert "2025-02-01 17:00:00" in response.text


def test_time_update():
    """
    Test that the time on the page updates every second.
    """
    response = client.get("/")
    first_time = response.text

    time.sleep(1)

    response = client.get("/")
    second_time = response.text

    assert first_time != second_time
