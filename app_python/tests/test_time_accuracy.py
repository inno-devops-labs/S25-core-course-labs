"""
This module contains tests for checking the
 accuracy of the time displayed on the application.
"""

from datetime import datetime
from pytz import timezone


def get_current_moscow_time():
    """
    Helper function to get the current time in Moscow.
    """
    moscow_tz = timezone('Europe/Moscow')
    return datetime.now(moscow_tz).strftime("%H:%M:%S")


def test_time_accuracy(client):
    """
    Test that the time displayed on
      the page matches the current time in Moscow.
    """
    generated_time = get_current_moscow_time()
    response = client.get('/')
    current_time = response.text.split("Current time in Moscow: ")[1][0:8]
    assert current_time == generated_time, \
        f"Expected time '{generated_time}', but got '{current_time}'."
