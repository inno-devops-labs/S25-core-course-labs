from datetime import datetime

import pytz
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from .config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
)


@app.get("/", response_class=HTMLResponse)
async def index():
    curr_time = datetime.now(pytz.timezone(settings.TIMEZONE))
    formatted_time = curr_time.strftime(settings.DATETIME_FORMAT)

    html_content = f"""<html>
    <head>
        <title>{settings.TIMEZONE} Time</title>
    </head>
    <body>
        <h1>Current time in {settings.TIMEZONE}: {formatted_time}</h1>
    </body>
</html>
    """

    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)
