from fastapi import FastAPI, Request
from datetime import datetime
import pytz
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(
        f"Incoming request: {request.method} {request.url.path} from {request.client.host}"
    )

    response = await call_next(request)

    logger.info(f"Outgoing response: Status {response.status_code}")
    return response


@app.get("/get_moscow_time")
def get_moscow_time():
    """
    Get the current time in Moscow, Russia.

    Returns:
        dict:
            - 'moscow_time': string in 'YYYY-MM-DD HH:MM:SS' format;
    """
    utc_now = datetime.now(pytz.utc)

    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = utc_now.astimezone(moscow_tz)

    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

    return {"moscow_time": formatted_time}
