import os
import pytest
from app import app as flask_app
from datetime import datetime
import pytz

@pytest.fixture
def app():
    # Set the testing environment variable
    os.environ['TESTING'] = 'true'
    yield flask_app
    # Clean up
    if os.path.exists('visits.txt'):
        os.remove('visits.txt')

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    """Test that home page returns 200 and contains expected content"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Current Time' in rv.data

def test_moscow_time_format():
    """Test that Moscow time is correctly formatted"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    assert len(moscow_time) == 19  # Format: YYYY-MM-DD HH:MM:SS

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'UP'