from prometheus_fastapi_instrumentator import Instrumentator

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import datetime
import pytz
import os


class Visits:
    VISITS_PATH = "./data/visits"

    def increment(self):
        self.visits += 1
        with open(Visits.VISITS_PATH, "w") as f:
            f.write(str(self.visits))

    def __init__(self):
        try:
            with open(Visits.VISITS_PATH, "r") as f:
                self.visits = int(f.read())
        except:
            self.visits = 0
            with open(Visits.VISITS_PATH, "w") as f:
                f.write(str(self.visits))


vis = Visits()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    vis.increment()
    current_date = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    return templates.TemplateResponse(
        request, "index.html", {"time": current_date.strftime("%H:%M")}
    )


Instrumentator().instrument(app).expose(app)
