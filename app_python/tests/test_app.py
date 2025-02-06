import pytest
import re
import time
from main import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Current time in Moscow" in response.data


def test_time_format(client):
    response = client.get('/')
    assert response.status_code == 200

    # Validate the time format YYYY-MM-DD HH:MM:SS
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", response.data.decode())
    assert match is not None, "Response does not contain a valid datetime format"


def test_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_headers(client):
    response = client.get('/')
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"


def test_response_time(client):
    start_time = time.time()
    response = client.get('/')
    end_time = time.time()

    assert response.status_code == 200
    assert (end_time - start_time) < 0.2, "Response time exceeds 200ms"
