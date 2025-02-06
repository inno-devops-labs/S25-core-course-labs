from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz

app = FastAPI()

MOSCOW_TZ = pytz.timezone("Europe/Moscow")


@app.get("/", response_class=HTMLResponse)
def get_moscow_time():
    moscow_time = datetime.now(MOSCOW_TZ).strftime("%d.%m.%Y %H:%M:%S")

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
            }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }}
            p {{
                font-size: 1.2rem;
            }}
        </style>
    </head>
    <body>
        <h1>Current Time in Moscow</h1>
        <p>{moscow_time}</p>
        <p>Refresh to update the time.</p>
    </body>
    </html>
    """
    return html_content
