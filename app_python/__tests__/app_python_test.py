from datetime import datetime
from fastapi.testclient import TestClient
import app
import pytz

client = TestClient(app.app)


def test_response_code():
    response = client.get("/")

    assert response.status_code == 200, "Something went wrong"


def test_html_for_validity():
    response = client.get("/")

    assert "<html>" in response.text, "html is not valid"
    assert "<head>" in response.text, "html is not valid"
    assert "Текущее Московское время" in response.text, "html is not valid"


def test_time_in_html_and_valid():
    response = client.get("/")

    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%H:%M:%S").split(":")

    assert (
        f"{current_time[0]}:{current_time[1]}" in response.text
    ), "Invalid time in html"
