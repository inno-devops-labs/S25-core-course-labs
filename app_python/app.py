from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import pytz
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") # specify the folder with static files
templates = Jinja2Templates(directory="./templates") # html template folder 

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    timezone = pytz.timezone('Europe/Moscow') # Selecting a time zone 
    time = datetime.now(timezone).strftime("%d-%m-%Y %H:%M:%S") 
    return templates.TemplateResponse("index.html", {"request": request, "msc_time": time})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=int(8000)) # ip address and port to run the web application 