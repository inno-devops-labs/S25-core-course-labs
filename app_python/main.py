from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.responses import HTMLResponse

app = FastAPI()


def create_time_string(timezone) -> str:
    now = datetime.now(timezone)
    return now.strftime("%H:%M:%S")


def create_response(time_string: str) -> HTMLResponse:
    html_content = f"""
    <!doctype html>
    <html>
        <head>
            <title>Time in Moscow</title>
        </head>
        <body>
            <p>Current time in Moscow is:</p>
            <p>{time_string}</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)


@app.get("/")
async def root() -> HTMLResponse:
    tz = pytz.timezone("Europe/Moscow")
    ts = create_time_string(tz)
    return create_response(ts)
