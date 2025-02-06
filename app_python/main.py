from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from datetime import datetime
import pytz

app = FastAPI(title="Moscow Time App", port=8000)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_moscow_time(request: Request):
    try:
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_tz)
        formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        return templates.TemplateResponse(
            request,
            "index.html",
            {"formatted_time": formatted_time}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
