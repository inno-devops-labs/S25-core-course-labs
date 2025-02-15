from fastapi.testclient import TestClient
from main import app
from datetime import datetime
import pytz

client = TestClient(app)


def test_get_moscow_time():
    response = client.get("/")
    assert response.status_code == 200
    assert "Current Time in Moscow" in response.text
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    assert current_time.tzname() in response.text


def test_response_html():
    response = client.get("/")
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_template_rendering():
    response = client.get("/")
    assert "time-container" in response.text
    assert "Refresh the page to update the time" in response.text
