from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
async def get_moscow_time():
    # Set the timezone to Moscow
    moscow_timezone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"Moscow Time": moscow_time}