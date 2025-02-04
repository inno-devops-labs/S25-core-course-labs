import pytest
from app import app
from datetime import datetime
import pytz
import re


@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    with app.test_client() as client:
        yield client


def test_homepage_status(client):
    """Test that the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200


def test_moscow_time_format(client):
    """Test that the Moscow time in response follows the correct format."""
    response = client.get('/')
    assert response.status_code == 200

    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", response.get_data(as_text=True))
    assert match is not None

    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time_moscow = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')

    assert current_time_moscow[:10] == match.group()[:10]
