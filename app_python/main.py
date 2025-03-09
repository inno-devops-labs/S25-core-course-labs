from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pytz
from app_python import create_time_string, create_time_response, create_visit_response, get_visit_count, increment_visit_count

app = FastAPI()


@app.get("/")
async def root() -> HTMLResponse:
    tz = pytz.timezone("Europe/Moscow")
    ts = create_time_string(tz)
    increment_visit_count()
    return create_time_response(ts)

@app.get("/visits")
async def visits():
    count = get_visit_count()
    return create_visit_response(count)
