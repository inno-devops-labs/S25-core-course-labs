import pytest
from datetime import datetime
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_moscow_time(client):
    resp = client.get('/')
    assert resp.status_code // 100 == 2
    assert b"Moscow time :" in resp.data

def test_time_format(client):
    resp = client.get('/')
    time = resp.data.decode().split("Moscow time : ")[1].strip()
    assert datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
