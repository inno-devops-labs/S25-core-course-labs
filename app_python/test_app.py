"""Tests for the Bottle application."""

import re
import threading
import time
import unittest
from datetime import datetime, timedelta
from subprocess import Popen

import pytest
import requests
from app import MSK_TIMEZONE, app

BASE_URL = "http://127.0.0.1:8080/"


def wait_for_server(url, timeout=5):
    """Utility function to wait for the server to be up."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            time.sleep(0.5)
    raise RuntimeError("Server did not start in time")


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

    def test_leap_year(self):
        """Test if the application handles leap years correctly."""
        leap_date = datetime(2024, 2, 29, tzinfo=MSK_TIMEZONE)
        formatted_date = leap_date.strftime("%d.%m.%Y")
        self.assertEqual(formatted_date, "29.02.2024")

    def test_midnight_rollover(self):
        """Test if the application correctly handles midnight rollover."""
        before_midnight = datetime(2025, 1, 1, 23, 59, 59, tzinfo=MSK_TIMEZONE)
        after_midnight = before_midnight + timedelta(seconds=1)
        self.assertEqual(after_midnight.strftime("%H:%M:%S"), "00:00:00")


@pytest.fixture(scope="module", autouse=True)
def start_server():
    """Fixture to start the Bottle server before tests and stop after."""

    with Popen(["python", "app.py"]) as process:
        wait_for_server(BASE_URL, timeout=5)
        yield
        process.terminate()


def test_root_route():
    """Test if the root route returns the correct HTML response."""
    response = requests.get(BASE_URL, timeout=5)

    # Verify response status and headers
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("text/html")

    # Verify response content
    assert "Current time and date in Moscow" in response.text
    assert re.search(r"<p>Time: \d{2}:\d{2}:\d{2}</p>", response.text)
    assert re.search(r"<p>Date: \d{2}\.\d{2}\.\d{4}</p>", response.text)


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
        wait_for_server(BASE_URL, timeout=5)

    @classmethod
    def tearDownClass(cls):
        """Stop the server."""
        cls.server_thread.join(0)

    def test_root_endpoint(self):
        """Test if the '/' endpoint returns the correct response."""
        response = requests.get(BASE_URL, timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current time and date in Moscow", response.text)
        self.assertIn("Time:", response.text)
        self.assertIn("Date:", response.text)
        self.assertRegex(response.text, r"<p>Time: \d{2}:\d{2}:\d{2}</p>")
        self.assertRegex(response.text, r"<p>Date: \d{2}\.\d{2}\.\d{4}</p>")
