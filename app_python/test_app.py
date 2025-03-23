import os
import tempfile
import pytest
from app import app


@pytest.fixture
def client(tmp_path):
    test_counter_file = tmp_path / "visits.txt"

    os.environ["COUNTER_FILE"] = str(test_counter_file)

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """
    Test that the home page loads successfully
    and contains the expected text."""
    response = client.get('/')

    assert response.status_code == 200

    assert b"Current Time in Moscow" in response.data
