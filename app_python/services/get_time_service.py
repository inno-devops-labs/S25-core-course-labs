import pytz
from datetime import datetime

from flask import render_template

class GetTimeService:
    """
    A service class to fetch the time.
    """

    @staticmethod
    def get_time_by_timezone(timezone: str) -> str:
        """
        Retrieves the current time in the specified timezone and renders it using a Flask template.
        
        Args:
            timezone (str): The timezone for which the current time is required.
        
        Returns:
            str: Rendered HTML template displaying the current time in the given timezone.
        """
        time_tz = pytz.timezone(timezone)
        current_time = datetime.now(time_tz).strftime('%Y-%m-%d %H:%M:%S')
        return render_template(f"current_time.html", current_time=current_time)