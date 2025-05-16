import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    return flask_app.test_client()

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    response = client.get('/')
    assert b"Current Time in Moscow" in response.data
