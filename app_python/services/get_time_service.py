import pytz
from datetime import datetime


class GetTimeService:
    """
    A service class to fetch the time.
    """

    @staticmethod
    def get_time_by_timezone(timezone: str) -> str:
        """
        Retrieves the current time in the specified timezone.

        Args:
            timezone (str): The timezone for which the current time is
            required.

        Returns:
            str: The current time in the given timezone formatted as
            'YYYY-MM-DD HH:MM:SS'.

        Raises:
            ValueError: If the provided timezone is invalid.
        """
        try:
            time_tz = pytz.timezone(timezone)
            return datetime.now(time_tz).strftime('%Y-%m-%d %H:%M:%S')
        except pytz.UnknownTimeZoneError as e:
            raise ValueError(f"Invalid timezone: {timezone}") from e
