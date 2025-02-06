import pytz
import re
from datetime import datetime


def test_homepage_response_status(server):
    response = server.get('/')
    assert response.status_code == 200


def test_show_time(server):
    response = server.get('/')
    assert "Current Time in Moscow:" in response.get_data(as_text=True)


def test_homepage_contains_valid_time(server, captured_templates):
    server.get('/')
    assert captured_templates, "Template was not rendered"

    _, context = captured_templates[0]
    assert 'current_time' in context, "current_time is missing in context"

    time_pattern = re.compile(r'\d{2}:\d{2}:\d{2}')
    assert time_pattern.match(context['current_time']), "Invalid time format"

    moscow_tz = pytz.timezone("Europe/Moscow")
    expected_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

    assert context['current_time'] == expected_time, \
        "Displayed time does not match Moscow time"


def test_template_rendering(server, captured_templates):
    response = server.get('/')
    assert response.status_code == 200
    assert len(captured_templates) == 1, "Template was not rendered"

    template, context = captured_templates[0]
    assert template.name == "index.html", "Wrong template used"
    assert "current_time" in context, "current_time is missing in context"
