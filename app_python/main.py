from datetime import datetime, time

import pytz
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Host and port to run the application
APP_HOST = "0.0.0.0"
APP_PORT = 8001

# Time format to display the time and an example of the time in this format
TIME_FORMAT = "%H:%M:%S"
TIME_FORMAT_EXAMPLE = "23:45:01"

# Timezone to display the time
TIMEZONE = "Europe/Moscow"

# HTML file with the web page
HTML_FILENAME = "index.html"

# Create a FastAPI application
app = FastAPI()


class TimeResponse(BaseModel):
    """
    Response model with a time field
    """
    time: time

    model_config = {
        # Custom JSON encoder for time objects to serialize
        # them as strings in the specified format
        "json_encoders": {time: lambda v: v.strftime(TIME_FORMAT)},

        # Custom JSON schema with an example
        "json_schema_extra": {"example": {"time": TIME_FORMAT_EXAMPLE}}
    }


@app.get("/", response_class=HTMLResponse)
def get_current_time_html():
    """
    Returns the HTML web page that displays the current time
    in the specified timezone using API
    """
    return HTMLResponse(open(HTML_FILENAME).read())


@app.get("/api/time", response_model=TimeResponse)
def get_current_time():
    """
    Returns the current time in the specified timezone
    """
    return TimeResponse(time=datetime.now(pytz.timezone(TIMEZONE)).time())


if __name__ == "__main__":
    # Run the application using Uvicorn
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
