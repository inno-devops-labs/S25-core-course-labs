from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/")
def get_time():
    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone)
    return {"moscow_time": time}
