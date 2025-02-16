from datetime import datetime, timezone, timedelta
import sys

import pytest

import app as app_python_app

"""
Primarily taken from https://flask.palletsprojects.com/en/stable/tutorial/tests/ and
then changed to be applicable to this project, as it is simpler than their example.
This is basically the arranging part.
"""


@pytest.fixture
def app():
    print(sys.path)
    this_app = app_python_app.app
    yield this_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_status(client, app):
    # Arranging is done mostly in conftest.py, so do not expect to see it much in here

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200


def test_current_time_text(client, app):
    # Act
    response = client.get('/')

    # Assert
    assert b'Current Time in Moscow:' in response.data


def test_the_time_in_moscow(client, app):
    # Arrange
    moscow_tz = timezone(timedelta(hours=3))  # Moscow timezone is UTC +3
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    # Act
    response = client.get('/')

    # Assert
    assert moscow_time.encode() in response.data


def test_the_time_in_london(client, app):
    # Arrange
    london_tz = timezone(timedelta(hours=0))  # London timezone is UTC +0
    london_time = datetime.now(london_tz)
    london_time_string = london_time.strftime('%Y-%m-%d %H:%M:%S')
    moscow_time = london_time + timedelta(hours=3)  # Changing to Moscow time
    moscow_time_string = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

    # Act
    response = client.get('/')

    # Assert
    assert not london_time_string.encode() in response.data
    assert moscow_time_string.encode() in response.data
