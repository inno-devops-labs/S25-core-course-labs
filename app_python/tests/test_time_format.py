"""
This module contains tests for checking the
 format of the time displayed on the application.
"""

import datetime
import pytest


def test_time_format(client):
    """
    Test that the time displayed on the page
      follows the expected format (HH:MM:SS).
    """
    response = client.get('/')
    current_time = response.text.split("Current time in Moscow: ")[1][0:8]
    try:
        datetime.datetime.strptime(current_time, "%H:%M:%S")
    except ValueError as e:
        pytest.fail(f"Time format is incorrect: {current_time}. Error: {e}")
