import pytest

from main import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'This is MSK time for now:' in response.data


def test_404_page(client):
    response = client.get("/kjasdlkaslkdhl")
    assert response.status_code == 404
    assert b"Page not found" in response.data
