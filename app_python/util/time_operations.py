from datetime import datetime
import pytz


def map_zone_to_timezone(zone: str) -> str:
    """Maps a zone to a timezone."""
    zone_to_tz = {
        "moscow": "Europe/Moscow",
    }
    if zone not in zone_to_tz:
        return None
    return zone_to_tz[zone]


def get_current_time(zone: str) -> str:
    """Returns the current time in a given zone as a formatted string."""
    given_timezone_str = map_zone_to_timezone(zone)
    if given_timezone_str is None:
        return "Invalid zone."
    given_timezone = pytz.timezone(given_timezone_str)
    current_time = datetime.now(given_timezone).strftime("%Y-%m-%d %H:%M:%S")
    return current_time
