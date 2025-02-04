import pytest
from app import app
from datetime import datetime
import pytz

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page returns 200 and contains expected content"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Current Time in Moscow' in rv.data

def test_moscow_time_format():
    """Test that Moscow time is correctly formatted"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    assert len(moscow_time) == 19  # Format: YYYY-MM-DD HH:MM:SS