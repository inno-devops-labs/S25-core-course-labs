from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pytz
from app_python import create_time_string, create_response

app = FastAPI()


@app.get("/")
async def root() -> HTMLResponse:
    tz = pytz.timezone("Europe/Moscow")
    ts = create_time_string(tz)
    return create_response(ts)
