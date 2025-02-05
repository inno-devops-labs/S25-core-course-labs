from datetime import datetime
import pytz
from utils.config import Config


def get_moscow_time() -> datetime:
    moscow_timezone = pytz.timezone(Config.TIMEZONE)
    current_utc_time = datetime.now(pytz.utc)
    moscow_time = current_utc_time.astimezone(moscow_timezone)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')
