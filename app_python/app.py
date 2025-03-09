import os
import logging
import pytz
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

COUNTER_PATH = "data/visit_count.txt"
# Set up logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def _store_count_file_if_needed():
    """
    Checks if the COUNTER_PATH file exists; if not, creates it with a zero count.
    Also creates the data folder if necessary.
    """
    if not os.path.exists(COUNTER_PATH):
        os.makedirs(os.path.dirname(COUNTER_PATH), exist_ok=True)
        with open(COUNTER_PATH, "w+") as file:
            file.write(str(0))
        logging.info("File visit_count.txt created with initial count = 0")


def _increment_visit_count():
    """
    Increments the visit count in the COUNTER_PATH file and returns the new count.
    """
    with open(COUNTER_PATH, "r+") as file:
        current = file.read().strip()
        visits = int(current) if current.isdigit() else 0
        visits += 1
        file.seek(0)
        file.write(str(visits))
        file.truncate()
    logging.info(f"New visit count set to {visits}")
    return visits


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Instrument the FastAPI app
instrumentator = Instrumentator()
instrumentator.instrument(app)
instrumentator.expose(app)


@app.on_event("startup")
def startup_event():
    _store_count_file_if_needed()


@app.get("/", response_class=HTMLResponse)
async def display_time(request: Request):
    """
    Displays the current Moscow time (UTC+3) and increments the visit counter.
    """
    try:
        _increment_visit_count()

        # Get the current Moscow time
        moscow_tz = pytz.timezone("Europe/Moscow")
        moscow_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

        return templates.TemplateResponse("index.html", {"request": request, "time": moscow_time})
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/error", response_class=HTMLResponse)
async def handle_error(request: Request):
    """
    Renders a generic error page.
    """
    return templates.TemplateResponse("error.html", {"request": request})


@app.get("/visits", response_class=PlainTextResponse)
async def display_visits():
    """
    Displays the current number of visits as plain text.
    """
    try:
        with open(COUNTER_PATH, "r") as file:
            visits = int(file.read().strip())
            logging.info(f"Displayed visit count: {visits}")
            return f"Number of visits: {visits}"
    except Exception as e:
        logging.error(f"An error occurred while reading visits: {e}")
        raise HTTPException(status_code=500, detail="Cannot read visit count")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8080)
