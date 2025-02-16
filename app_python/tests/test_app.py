from datetime import datetime

import pytest
from freezegun import freeze_time
from flask import template_rendered

from app import app, get_current_time, TIMEZONE


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def captured_templates():
    recorded = []

    def record(sender, template, context, *extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_time_page_status_code(client):
    response = client.get('/')

    assert response.status_code == 200


def test_get_current_time_format():
    current_time = get_current_time(TIMEZONE)

    try:
        datetime.strptime(current_time, '%d-%m-%Y %H:%M:%S')
    except ValueError:
        pytest.fail('get_current_time does not return the time in the expected format')


@freeze_time('2015-04-03 12:13:14', tz_offset=-3)
def test_time_page_correct_time_and_timezone(client, captured_templates):
    response = client.get('/')

    assert response.status_code == 200

    assert captured_templates, 'No template was rendered'

    _, context = captured_templates[0]

    assert context['time'] == '03-04-2015 12:13:14', (
        'Time value in context does not match expected time'
    )
    assert context['timezone'] == TIMEZONE, (
        'Timezone value in context does not match expected timezone'
    )
