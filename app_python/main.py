from datetime import datetime, time

import pytz
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

TIME_FORMAT = "%H:%M:%S"
TIMEZONE = "Europe/Moscow"

HTML_FILENAME = "index.html"

app = FastAPI()


class TimeResponse(BaseModel):
    time: time

    model_config = {
        "json_encoders": {time: lambda v: v.strftime(TIME_FORMAT)},
        "json_schema_extra": {"example": {"time": "23:45:01"}}
    }


@app.get("/", response_class=HTMLResponse)
def get_current_time_html():
    return HTMLResponse(open(HTML_FILENAME).read())


@app.get("/api/time", response_model=TimeResponse)
def get_current_time():
    return TimeResponse(time=datetime.now(pytz.timezone(TIMEZONE)).time())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
