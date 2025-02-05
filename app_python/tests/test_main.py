import pytest
from app_python.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_msk_time_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Current time in Moscow' in response.data
