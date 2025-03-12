import pytz
import re
from app_python import create_time_string, create_time_response


def test_create_time_string():
    tz = pytz.timezone("Europe/Moscow")
    time_string = create_time_string(tz)
    assert re.match("[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}",
        time_string) is not None


def _check_response(time_string: str) -> bool:
    resp = create_time_response(time_string)
    content = str(resp.body)
    if time_string not in content:
        return False

    return True


def test_create_response():
    assert _check_response("abcd") is True
    assert _check_response("blahblahblah") is True
    assert _check_response("Hello World!") is True
    assert _check_response("04:20:00") is True
    assert _check_response("hola") is True
    assert _check_response("[object Object]") is True
