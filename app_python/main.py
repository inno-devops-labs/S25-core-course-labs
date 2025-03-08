from fastapi import FastAPI
from datetime import datetime
import pytz
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response


app = FastAPI()


@app.get("/")
def get_time():
    timezone = pytz.timezone("Europe/Moscow")
    time = datetime.now(timezone)
    return {"moscow_time": time}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
