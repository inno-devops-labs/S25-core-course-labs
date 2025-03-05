from fastapi import FastAPI
from datetime import datetime
import pytz
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

app = FastAPI()

VISITS_FILE = "visits.txt"

def read_visits() -> int:
    """Read the current visit count from the visits file.
    Returns 0 if the file does not exist or an error occurs.
    """
    if os.path.exists(VISITS_FILE):
        try:
            with open(VISITS_FILE, "r") as f:
                count = int(f.read().strip())
            return count
        except Exception as e:
            logging.error(f"Error reading visits file: {e}")
            return 0
    else:
        return 0

def write_visits(count: int) -> None:
    """Write the updated visit count to the visits file."""
    try:
        with open(VISITS_FILE, "w") as f:
            f.write(str(count))
    except Exception as e:
        logging.error(f"Error writing visits file: {e}")

def get_moscow_time() -> str:
    """Retrieve the current time in Moscow."""
    logging.info("Getting current Moscow time...")
    try:
        moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
        current_time = moscow_time.strftime("%H:%M:%S")
        logging.info(f"Successfully got time in Moscow: {current_time}")
        return current_time
    except Exception as e:
        logging.error("Failed to get current Moscow time!")
        return f"Error: {str(e)}"

@app.get("/")
def read_root() -> dict:
    logging.info("HTTP GET request received at /")
    # Read the current visit count, increment, and write it back
    count = read_visits()
    count += 1
    write_visits(count)
    
    moscow_time = get_moscow_time()
    return {
        "message": f"The current time in Moscow is {moscow_time}. This page has been accessed {count} times."
    }

@app.get("/visits")
def get_visits() -> dict:
    logging.info("HTTP GET request received at /visits")
    count = read_visits()
    return {"visits": count}
