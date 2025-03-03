import pytest
import app.app as flask_app

from bs4 import BeautifulSoup
from flask.testing import FlaskClient
from datetime import datetime, timezone, timedelta


def test_availability(client: FlaskClient) -> None:
    """
    Pytest test availability
    """
    response = client.get("/")
    assert response.status_code == 200


def test_html(client: FlaskClient) -> None:
    """
    Pytest test HTML contents
    """
    response = client.get("/").text
    assert "Moscow" in response, "Html is broken"


def test_time(client: FlaskClient) -> None:
    """
    Pytest test Moscow time for correctness within the <p id="time" class="time"> tag
    """
    response = client.get("/").text
    soup = BeautifulSoup(response, "html.parser")
    time_tag = soup.find("p", {"id": "time", "class": "time"})
    assert time_tag is not None, "Time tag is missing"

    zone = timezone(timedelta(hours=3))
    time = datetime.now(timezone.utc).astimezone(zone)
    formatted_time = time.strftime("%H:%M:%S %d.%m.%Y")

    assert formatted_time in time_tag.text, "Time is broken"


@pytest.fixture
def client():
    test_app = flask_app.create_flask_app()
    test_app.config["TESTING"] = True
    return test_app.test_client()
