'''python web-app program'''
import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import pytz

app = FastAPI()
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
# specify the folder with static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR) # html template folder

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    '''Displaying Moscow time'''
    timezone = pytz.timezone('Europe/Moscow') # Selecting a time zone
    time = datetime.now(timezone).strftime("%d-%m-%Y %H:%M:%S")
    return templates.TemplateResponse(request, "index.html", {"msc_time": time})

if __name__ == "__main__":
    # ip address and port to run the web application
    uvicorn.run(app, host="127.0.0.1", port=int(8000))
