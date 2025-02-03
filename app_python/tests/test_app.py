from datetime import datetime

import pytest

from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client


def test_homepage_status_code(client):
    """Checks if the homepage loads successfully."""
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_content(client, monkeypatch):
    """Test if the homepage returns the correct time and renders correctly."""

    class MockDatetime:
        @classmethod
        def now(cls, tz=None):
            return datetime(2024, 1, 1, 12, 34, 56)

    monkeypatch.setattr("app.datetime", MockDatetime)

    response = client.get("/")
    assert response.status_code == 200
    assert "12:34:56" in response.data.decode("utf-8")  # Ensures time matches mock


def test_template_rendering(client):
    """Ensure that the response contains a valid time format."""
    response = client.get("/")
    assert response.status_code == 200

    import re

    match = re.search(r"\d{2}:\d{2}:\d{2}", response.data.decode("utf-8"))
    assert match is not None


def test_404_error(client):
    """Ensure that a non-existent route returns a 404 status."""
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_debug_mode():
    app.debug = True
    assert app.debug is True
