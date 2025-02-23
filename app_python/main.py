import logging
import sys
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz

app = FastAPI()
templates = Jinja2Templates(directory="templates")

logger = logging.getLogger("my_app")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s '
                              '- %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


# Log request information
@app.middleware("http")
async def log_request_info(request: Request, call_next):
    logger.info(f"Received request: {request.method} "
                f"{request.url} from {request.client.host}")
    response = await call_next(request)
    return response


@app.get("/", response_class=HTMLResponse)
async def read_time(request: Request):
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse(
        request,
        "index.html",
        {"time": formatted_time}
    )
