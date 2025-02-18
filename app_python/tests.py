import pytest
from main import app
from datetime import datetime
import pytz

@pytest.fixture
def client():
    return app.test_client()

def test_returns_html_page(client):
    response = client.get('/')
    assert 'text/html' in response.content_type

def test_index_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_time_format(client):
    response = client.get('/')
    time = response.get_data(as_text=True)
    current_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y.%m.%d %H:%M:%S")
    assert current_time in time
