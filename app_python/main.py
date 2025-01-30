from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

import pytz

'''
FastAPI entity
'''
app = FastAPI(
    title="Region Time API",
    version="0.0.1"
)

'''
Function for getting the current time in the specified as the argument region
'''
def get_location_time(region):
      try:
          return datetime.now(pytz.timezone(region))
      except pytz.UnknownTimeZoneError:
          raise ValueError(f"Invalid timezone: {region}")

'''
Endpoint function for getting the current moscow time with some simple html design
'''
@app.get("/time/moscow", response_class=HTMLResponse)
async def getTime():
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
        <h1><b>Current Time in Moscow:</b> {get_location_time("Europe/Moscow")}</h1>
        <img src="https://kudamoscow.ru/uploads/9151b31fb2ef1543969b65e6bc111bea.png" alt="Moscow Image">
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)