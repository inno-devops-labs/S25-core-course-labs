import datetime as dt
import pytz

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# Initialize FastAPI app
app = FastAPI()

# Set up Jinja2 for rendering templates
templates = Jinja2Templates(directory="templates")

def get_moscow_time():
    """Returns the current time in Moscow as a dictionary."""
    now = dt.datetime.now(pytz.timezone('Europe/Moscow'))
    return {"hours": now.hour, "minutes": now.minute, "seconds": now.second}

@app.get("/", response_class=HTMLResponse)
async def show_moscow_time(request: Request):
    """Renders the Moscow time page."""
    time_data = get_moscow_time()
    return templates.TemplateResponse("index.html", {"request": request, **time_data})
