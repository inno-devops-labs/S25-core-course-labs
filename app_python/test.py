import sys
import pytest

from datetime import datetime, timezone, timedelta

import app as tested_app

ROOT_PATH='/'
RANDOM_PATH='/random/path'
STRING_ON_PAGE="Moscow"
ANOTHER_TIMEZONE=-2
ANOTHER_DATE_FORMAT="%Y %M:%H:%S %b %a %d"
TIME_ERROR_MARGIN=1

@pytest.fixture
def app():
    flask_app = tested_app.app
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

# Tests that the page is accessible
def test_root_response_correct(client, app):
    response = client.get(ROOT_PATH)
    
    assert response.status_code == 200

# Tests that the page does not load correcly when having a random path
def test_non_root_response_incorrect(client, app):
    response = client.get(RANDOM_PATH)
    
    assert response.status_code != 200

# Tests that the page has relevant text
def test_page_contents_have_relevant_text(client, app):
    response = client.get(ROOT_PATH)
    
    assert STRING_ON_PAGE.encode() in response.data

# Tests that the current time does show on page with 1 second margin of error
def test_time_in_moscow_shows_on_page(client, app):
    needed_time = datetime.now(timezone(timedelta(hours=tested_app.TIMEZONE)))
    needed_times = [(needed_time + timedelta(seconds=error_margin))
                    .strftime(tested_app.DATE_FORMAT).encode()
                    for error_margin in range(-TIME_ERROR_MARGIN,
                                              TIME_ERROR_MARGIN+1)]
    
    response = client.get(ROOT_PATH)

    assert any([i in response.data for i in needed_times])

# Tests that the time shown on page can be changed by changing the timezone
def test_timezone_parameter_change_affects_page(client, app):
    tested_app.TIMEZONE = ANOTHER_TIMEZONE
    
    needed_time = datetime.now(timezone(timedelta(hours=tested_app.TIMEZONE)))
    needed_times = [(needed_time + timedelta(seconds=error_margin))
                    .strftime(tested_app.DATE_FORMAT).encode()
                    for error_margin in range(-TIME_ERROR_MARGIN,
                                              TIME_ERROR_MARGIN+1)]
    
    response = client.get(ROOT_PATH)

    assert any([i in response.data for i in needed_times])

# Tests that the time shown on page can be changed by changing the template
def test_date_format_change_affects_page(client, app):
    tested_app.DATE_FORMAT = ANOTHER_DATE_FORMAT
    
    needed_time = datetime.now(timezone(timedelta(hours=tested_app.TIMEZONE)))
    needed_times = [(needed_time + timedelta(seconds=error_margin))
                    .strftime(tested_app.DATE_FORMAT).encode()
                    for error_margin in range(-TIME_ERROR_MARGIN,
                                              TIME_ERROR_MARGIN+1)]
    
    response = client.get(ROOT_PATH)

    assert any([i in response.data for i in needed_times])
