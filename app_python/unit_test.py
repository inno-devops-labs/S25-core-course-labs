"""
Unit tests
"""
import pytest
from web import app


@pytest.fixture
def client():
    """
    testing
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """
    Testing that main page loads and contains time
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Current time" in response.data
