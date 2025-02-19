import pytest
import app
from datetime import datetime
import re
import pytz


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index_contains_time(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Moscow Time" in response.data

    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%H:%M")
    assert re.search(rf"{current_time}:\d{{2}}", response.text)


def test_index_content_type(client):
    response = client.get("/")
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"


def test_index_html_structure(client):
    response = client.get("/")
    assert b"<title>" in response.data
    assert b"</title>" in response.data
    assert b"<body>" in response.data
    assert b"</body>" in response.data


def test_post_not_allowed(client):
    response = client.post("/")
    assert response.status_code == 405
