import sys
import pytest

from datetime import datetime, timezone, timedelta

import app as tested_app

@pytest.fixture
def app():
    app = tested_app.app
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_root_response(client, app):
    assert client.get('/').status_code == 200

def test_non_root_response(client, app):
    assert client.get('/random/path').status_code != 200

def test_page_contents(client, app):
    response = client.get('/')
    assert b'Moscow' in response.data

# Tests that the current time does show on page with 1 second margin of error
def test_time_in_moscow(client, app):
    needed_time = datetime.now(timezone(timedelta(hours=tested_app.TIMEZONE)))
    needed_time_plus_1 = needed_time + timedelta(seconds=1)
    needed_time_minus_1 = needed_time - timedelta(seconds=1)
    needed_times = [needed_time.strftime(tested_app.DATE_FORMAT).encode(),
                    needed_time_plus_1.strftime(tested_app.DATE_FORMAT).encode(),
                    needed_time_minus_1.strftime(tested_app.DATE_FORMAT).encode()]
    
    response = client.get('/')

    assert any([i in response.data for i in needed_times])

# Tests that the time shown on page can be changed by changing the timezone
def test_time_new_timezone(client, app):
    tested_app.TIMEZONE = -2
    
    needed_time = datetime.now(timezone(timedelta(hours=tested_app.TIMEZONE)))
    needed_time_plus_1 = needed_time + timedelta(seconds=1)
    needed_time_minus_1 = needed_time - timedelta(seconds=1)
    needed_times = [needed_time.strftime(tested_app.DATE_FORMAT).encode(),
                    needed_time_plus_1.strftime(tested_app.DATE_FORMAT).encode(),
                    needed_time_minus_1.strftime(tested_app.DATE_FORMAT).encode()]
    
    response = client.get('/')

    assert any([i in response.data for i in needed_times])
