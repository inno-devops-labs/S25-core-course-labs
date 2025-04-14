from datetime import datetime
import pytz
from config import TIMEZONE


def get_time(time=TIMEZONE):
    moscow_tz = pytz.timezone(time)
    current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")
    return current_time
