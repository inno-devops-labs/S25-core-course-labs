from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/")
def get_moscow_time():
    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"moscow_time": time}
