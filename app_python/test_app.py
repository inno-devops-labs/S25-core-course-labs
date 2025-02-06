import pytest
from time_app import app

##
# test comment
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Current Time in Moscow" in response.data


def test_moscow_time_format(client):
    response = client.get("/")
    assert response.status_code == 200
    assert len(response.data.decode().split()) > 0
