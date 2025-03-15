from prometheus_fastapi_instrumentator import Instrumentator

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import datetime
import pytz

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    current_date = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    return templates.TemplateResponse(
        request, "index.html", {"time": current_date.strftime("%H:%M")}
    )


Instrumentator().instrument(app).expose(app)
