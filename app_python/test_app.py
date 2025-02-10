import pytest
from app import app

@pytest.fixture
def client():
    # Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_status(client):
    """Test that homepage returns HTTP 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_content(client):
    """Test that homepage contains 'Current Time in Moscow'."""
    response = client.get('/')
    assert b'Current time in Moscow:' in response.data
import pytest
from app import app

@pytest.fixture
def client():
    # Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_status(client):
    """Test that homepage returns HTTP 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_content(client):
    """Test that homepage contains 'Current Time in Moscow'."""
    response = client.get('/')
    assert b'Current time in Moscow:' in response.data
import pytest
from app import app

@pytest.fixture
def client():
    # Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_status(client):
    """Test that homepage returns HTTP 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_content(client):
    """Test that homepage contains 'Current Time in Moscow'."""
    response = client.get('/')
    assert b'Current time in Moscow:' in response.data
