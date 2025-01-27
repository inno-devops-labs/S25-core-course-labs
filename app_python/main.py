from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz

app = FastAPI()

def create_response(time: str) -> HTMLResponse:
    html_content = f"""
    <html>
        <head>
            <title>Moscow time</title>
        </head>
        <body>
            <p>Time in Moscow</p>
            <p>{time}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/")
async def root():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    str_current_time = current_time.strftime("%H:%M:%S")
    return create_response(str_current_time)