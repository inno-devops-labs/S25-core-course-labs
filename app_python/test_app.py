import pytest
import tempfile
import os
from datetime import datetime
from app import create_app


@pytest.fixture(autouse=True)
def setup_test_env(monkeypatch):
    tmpdir = tempfile.TemporaryDirectory()
    test_file = os.path.join(tmpdir.name, 'visits.txt')
    monkeypatch.setenv('VISITS_FILE', test_file)

    with open(test_file, 'w') as f:
        f.write('0')

    yield
    tmpdir.cleanup()


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_moscow_time(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"Moscow time:" in resp.data
    time_str = resp.data.decode().split("Moscow time: ")[1].strip('</h1>')
    datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')


def test_visits_counter(client):
    resp = client.get('/visits')
    assert b"Total visits: 0" in resp.data
    client.get('/')
    client.get('/')
    resp = client.get('/visits')
    assert b"Total visits: 2" in resp.data