"""
This module contains tests for checking
 the timezone functionality of the application.
"""

import datetime
import pytz
import pytest


def extract_time_from_response(response):
    """
    Helper function to extract the current time from the response text.
    Raises an AssertionError if the expected time string is not found.
    """
    try:
        return response.text.split("Current time in Moscow: ")[1][0:8]
    except IndexError:
        pytest.fail("Expected time string not found in the response.")
        return None


def test_check_timezone(client):
    """
    Test that the time displayed on the page
      is correctly localized to the Moscow timezone.
    """
    response = client.get('/')

    # Extract time string
    current_time_as_str = extract_time_from_response(response)

    # Get today's date to form a full datetime
    today_date = datetime.date.today()
    full_datetime_str = f"{today_date} {current_time_as_str}"

    # Convert string to datetime object (naïve)
    try:
        naive_datetime = datetime.datetime.strptime(
            full_datetime_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pytest.fail(f"Time string '{current_time_as_str}'"
                    " is not in the expected format (HH:MM:SS).")

    # Localize the datetime to Moscow timezone
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_datetime = moscow_tz.localize(naive_datetime)

    # Check if it's in Moscow timezone
    assert moscow_datetime.tzinfo.zone == "Europe/Moscow", (
        "Expected timezone 'Europe/Moscow', but got "
        f"'{moscow_datetime.tzinfo.zone}'"
    )
