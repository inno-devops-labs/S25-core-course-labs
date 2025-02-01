"""
This module contains fixtures for testing the Flask application.
"""

import pytest
from app import create_app


@pytest.fixture
def app_instance():
    """
    Fixture to create and configure the Flask app instance for testing.
    """
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app


@pytest.fixture
def client(app_instance):
    """
    Fixture to create a test client for making requests to the app.
    """
    return app_instance.test_client()
