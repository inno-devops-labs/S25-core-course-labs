from datetime import datetime

import pytz
from flask.testing import FlaskClient


def test_availability(client: FlaskClient) -> None:
    """
    Pytest test availability.
    """
    response = client.get("/")
    success_status_code = 200
    assert response.status_code == success_status_code


def test_html(client: FlaskClient) -> None:
    """
    Test HTML contents.
    """
    response = client.get("/").text
    assert "Moscow" in response, "HTML is incorrect"


def test_time(client: FlaskClient) -> None:
    """
    Pytest test Moscow time for correctness.
    """
    response = client.get("/").text

    moscow_timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(moscow_timezone)

    time_without_ms = str(time).split(".", maxsplit=1)[0]

    assert time_without_ms in response, "Time is incorrect"
