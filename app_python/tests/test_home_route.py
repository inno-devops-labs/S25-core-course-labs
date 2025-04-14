"""
This module contains tests for the home route of the application.
"""


def test_home_route(client):
    """
    Test that the home route ('/') returns a 200 status code.
    """
    response = client.get('/')
    assert response.status_code == 200, \
        f"Expected status code 200, but got {response.status_code}."
