"""
This module contains test cases for the Python Web Application.
"""

from datetime import datetime, timezone, timedelta
from fastapi.testclient import TestClient
from fastapi.templating import Jinja2Templates
from main import app

client = TestClient(app)


def test_root_endpoint():
    """
    Test the root endpoint ("/") to ensure:
    1. The response is successful (status code 200)
    2. The response is an HTML response
    3. The current time is displayed correctly
    """
    response = client.get("/")

    assert response.status_code == 200

    assert "text/html" in response.headers.get("content-type", "")

    zone = timezone(timedelta(hours=3))
    time = datetime.now(timezone.utc).astimezone(zone)

    assert str(time.replace(microsecond=0)).split("+", maxsplit=1)[0] in response.text


def test_static_files_served():
    """
    Verify that static files can be served from the /static directory.
    Note: This assumes you have at least one static file in the directory.
    """
    response = client.get("/static/styles.css")
    assert response.status_code == 200

    response = client.get("/static/item.html")
    assert response.status_code == 404


def test_templates_configured():
    """
    Verify that Jinja2 templates are correctly configured.
    """

    try:
        templates = Jinja2Templates(directory="templates")
        assert templates is not None
    except ImportError as e:
        assert False, f"Failed to configure Jinja2 templates: {e}"
