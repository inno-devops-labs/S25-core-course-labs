from fastapi import FastAPI
from datetime import datetime
from prometheus_fastapi_instrumentator import Instrumentator
import pytz

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/time")
def get_moscow_time():
    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"moscow_time": time}
