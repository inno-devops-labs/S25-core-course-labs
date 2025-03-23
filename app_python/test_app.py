import pytest
from app import app


@pytest.fixture
def client():
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_counter_file = os.path.join(tmpdirname, "visits.txt")

        from app import counter_file
        globals()['counter_file'] = test_counter_file

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
