from fastapi import FastAPI
from datetime import datetime
import pytz
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

app = FastAPI()


def get_moscow_time() -> str:
    logging.info("Getting current Moscow time...")
    try:
        moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
        currrent_time = moscow_time.strftime("%H:%M:%S")
        logging.info(f"Sucessfully got time in Moscow: {currrent_time}")
        return currrent_time
    except Exception as e:
        logging.info("Failed to get current Moscow time!")
        return f"Error: {str(e)}"


@app.get("/")
def read_root() -> dict[str, str]:
    logging.info("HTTP GET request sent!")
    moscow_time = get_moscow_time()
    return {"message": f"The current time in Moscow is {moscow_time}"}
