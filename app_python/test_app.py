import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_content(client):
    response = client.get('/')
    assert b"Current Time in Moscow" in response.data
