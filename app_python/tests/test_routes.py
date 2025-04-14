import datetime

from routes import get_time
from schemas import TimeResponse


def test_get_time(mocker):
    now = datetime.datetime.now()
    mocked_dt = mocker.patch(
            "datetime.datetime",
    )
    mocked_dt.now.return_value = now
    response = get_time()
    assert response == TimeResponse(
            time=now,
    )
