"""Tests for the Bottle application."""

import threading
import time
import unittest
from datetime import datetime, timedelta
from subprocess import Popen

import pytest
import requests
from app import MSK_TIMEZONE, app


class TestAppUnit(unittest.TestCase):
    """Unit tests for the Bottle application."""

    def test_msk_timezone(self):
        """Test if the Moscow timezone is correctly set."""
        self.assertEqual(MSK_TIMEZONE.utcoffset(None), timedelta(hours=3))

    def test_show_time_format(self):
        """Test if the time is formatted correctly."""
        now = datetime(2025, 1, 1, 15, 30, 45, tzinfo=MSK_TIMEZONE)
        formatted_time = now.strftime("%H:%M:%S")
        self.assertEqual(formatted_time, "15:30:45")

    def test_show_date_format(self):
        """Test if the date is formatted correctly."""
        now = datetime(2025, 1, 1, tzinfo=MSK_TIMEZONE)
        formatted_date = now.strftime("%d.%m.%Y")
        self.assertEqual(formatted_date, "01.01.2025")


# Define the base URL for the local server
BASE_URL = "http://127.0.0.1:8080/"


@pytest.fixture(scope="module", autouse=True)
def start_server():
    """Fixture to start the Bottle server before tests and stop after."""

    # Start the Bottle app as a subprocess
    with Popen(["python", "app.py"]) as process:
        time.sleep(3)  # Wait for the server to start up
        yield  # This marks the point where the test code runs
        process.terminate()  # Stop the server after tests


def test_root_route():
    """Test if the root route returns the correct HTML response."""
    # Make a request to the root route
    response = requests.get(BASE_URL, timeout=5)

    # Check the status code
    assert response.status_code == 200

    # Check that the response contains the expected HTML content
    assert "Current time and date in Moscow" in response.text
    assert "Time:" in response.text
    assert "Date:" in response.text

    # Additional checks for the format of the time and date
    assert (
        len(response.text.split("<p>Time: ")[1].split("</p>")[0]) == 8
    )  # Time format H:M:S
    assert (
        len(response.text.split("<p>Date: ")[1].split("</p>")[0]) == 10
    )  # Date format dd.mm.yyyy


class TestAppE2E(unittest.TestCase):
    """End-to-end tests for the Bottle application."""

    @classmethod
    def setUpClass(cls):
        """Start the server in a separate thread."""
        cls.server_thread = threading.Thread(
            target=lambda: app.run(
                host="127.0.0.1", port=8080, debug=False, quiet=True
            ),
            daemon=True,
        )
        cls.server_thread.start()
        time.sleep(1)  # Give the server time to start

    @classmethod
    def tearDownClass(cls):
        """Stop the server."""
        cls.server_thread.join(0)

    def test_root_endpoint(self):
        """Test if the '/' endpoint returns the correct response."""
        response = requests.get("http://127.0.0.1:8080/", timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current time and date in Moscow", response.text)
        self.assertIn("Time:", response.text)
        self.assertIn("Date:", response.text)
