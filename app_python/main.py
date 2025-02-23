from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_time(request: Request):
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse(
        request,
        "index.html",
        {"time": formatted_time}
    )
