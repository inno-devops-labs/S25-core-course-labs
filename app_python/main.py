from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz
import logging
from prometheus_fastapi_instrumentator import Instrumentator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Create a logger instance
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Region Time API",
    version="0.0.1"
)

link = "https://kudamoscow.ru/uploads/9151b31fb2ef1543969b65e6bc111bea.png"

Instrumentator().instrument(app).expose(app)

def get_location_time(region):
    """
    Function for getting the current time in the specified timezone.
    """
    try:
        return datetime.now(pytz.timezone(region))
    except pytz.UnknownTimeZoneError as e:
        logger.error(f"Invalid timezone: {region}")  # Log the error
        raise ValueError(f"Invalid timezone: {region}")

@app.get("/time/moscow", response_class=HTMLResponse)
async def getTime():
    """
    Endpoint function for getting the current Moscow time with HTML design.
    """
    logger.info("Accessing /time/moscow endpoint")

    try:
        time = get_location_time("Europe/Moscow")
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Moscow Time</title>
            <style>
                body {{
                    text-align: center;
                    font-family: Arial, sans-serif;
                    margin-top: 50px;
                }}
                img {{
                    margin-top: 20px;
                    max-width: 100%;
                    height: auto;
                }}
            </style>
        </head>
        <body>
            <h1><b>Current Time in Moscow:</b> {time}</h1>
            <img src="{link}" alt="Moscow Image">
        </body>
        </html>
        """
        logger.info("Successfully generated response for /time/moscow")  # Log success
        return HTMLResponse(content=html_content)

    except Exception as e:
        logger.error(f"Error occurred while processing /time/moscow: {e}")  # Log errors
        raise HTTPException(status_code=500, detail="Internal Server Error")