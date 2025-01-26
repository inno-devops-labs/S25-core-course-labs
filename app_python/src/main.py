from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/get_moscow_time")
def get_moscow_time():
    """
    Get the current time in Moscow, Russia.
    
    Returns:
        dict:
            - 'moscow_time': string in 'YYYY-MM-DD HH:MM:SS' format;
    """
    utc_now = datetime.now(pytz.utc)

    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = utc_now.astimezone(moscow_tz)

    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

    return {"moscow_time": formatted_time}
