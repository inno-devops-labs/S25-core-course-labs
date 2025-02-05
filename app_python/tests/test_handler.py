from datetime import datetime
import re
import pytz


def test_homepage_status_code(server):
    response = server.get('/')
    assert response.status_code == 200


def test_homepage_content(server):
    response = server.get('/')
    assert b'Current Time in Moscow' in response.data


def test_homepage_contains_valid_time(server, captured_templates):
    server.get('/')
    assert captured_templates, "Template was not rendered"
    _, context = captured_templates[0]
    assert 'current_time' in context, "current_time is missing in context"

    # Validate timestamp format YYYY-MM-DD HH:MM:SS
    time_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    assert time_pattern.match(
        context['current_time']), "Invalid timestamp format"


def test_homepage_timezone(server, captured_templates):
    server.get('/')
    assert captured_templates, "Template was not rendered"
    _, context = captured_templates[0]

    moscow_tz = pytz.timezone('Europe/Moscow')
    expected_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    response_time = context['current_time']

    assert abs(datetime.strptime(response_time, "%Y-%m-%d %H:%M:%S")
               - datetime.strptime(expected_time, "%Y-%m-%d %H:%M:%S")
               ).seconds < 5, "Time mismatch in Moscow timezone"
