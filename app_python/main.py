from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz
import logging
import os

app = FastAPI()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

VISITS_FILE = "/data/visits"
DATA_DIR = os.path.dirname(VISITS_FILE)

os.makedirs(DATA_DIR, exist_ok=True)

def get_visits():
    try:
        with open(VISITS_FILE, "r") as file:
            return int(file.read().strip()) 
    except FileNotFoundError:
        return 0


def update_visits(count):
    with open(VISITS_FILE, "w") as file:
        file.write(str(count))


def create_response(time: str) -> HTMLResponse:
    logging.info("Creating HTML response")
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
    try:
        logging.info("Request received at the root endpoint")
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz)
        str_current_time = current_time.strftime("%H:%M:%S")

        count = get_visits() + 1
        update_visits(count)

        return create_response(str_current_time)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return HTMLResponse(content="<p>Error</p>", status_code=500)


@app.get("/visits")
async def visits():
    count = get_visits()
    return {"Total Visits": count}