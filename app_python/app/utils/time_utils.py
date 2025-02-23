from datetime import datetime, timedelta, timezone


def get_moscow_time():
    """Returns the current time in Moscow."""
    utc_time = datetime.now(timezone.utc)
    moscow_offset = timedelta(hours=3)  # UTC+3
    moscow_time = utc_time + moscow_offset
    return moscow_time.strftime("%Y-%m-%d %H:%M:%S")
