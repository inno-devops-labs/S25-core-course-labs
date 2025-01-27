from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_moscow_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%H:%M:%S").split(':')

    html_content = f"""
    <html>
        <head>
            <title>Текущее Московское время</title>
        </head>
        <body style="display: flex; justify-content: center; align-items: center; font-family: Poppins, sans-serif; background-color: #222; height: 100vh; overflow: hidden; font-weight: 700;">
            <div style="display: inline-flex; justify-content: center;">
              <p style="font-size: 154px; color: #fbcb40; margin: 0;">{current_time[0]}:{current_time[1]}</p>
              <p style="color: white; font-size: 72px; margin: 15px 0 0 0;">{current_time[2]}</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)