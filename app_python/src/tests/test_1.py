"""
Test 1 for the web application.

- `test_read_time`: tests the web page containing current time in Moscow
"""

from fastapi.testclient import TestClient
from bs4 import BeautifulSoup
from src.main import app
from src.utils import get_time


client = TestClient(app)


def test_read_time():
    """Tests the web page containing current time in Moscow."""
    response = client.get("/")
    assert response.status_code == 200
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.find("span", id="time").text == get_time().strftime("%d.%m.%Y %H:%M:%S")
