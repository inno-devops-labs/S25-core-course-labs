import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_current_time_status_code(client):
    response = client.get("/")
    assert response.status_code == 200

def test_current_time_content(client):
    response = client.get("/")
    assert b"Current time in Moscow" in response.data
