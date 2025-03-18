from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz
import os

app = FastAPI()

VISITS_FILE = "/data/visits.txt"


def get_visits():
    """Reads the visit count from a file."""
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_visits(count):
    """Writes the visit count to a file."""
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


@app.get("/", response_class=HTMLResponse)
async def get_time():
    """Shows current Moscow time and increases visit count."""
    msk_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(msk_timezone).strftime("%Y-%m-%d %H:%M:%S")


    count = get_visits() + 1
    save_visits(count)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Moscow Time</title>
    </head>
    <body>
        <h1>Current Time in Moscow:</h1>
        <p>{current_time}</p>
        <h2>Visit Count: {count}</h2>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/visits")
async def visits():
    """Returns the total number of visits."""
    count = get_visits()
    return {"total_visits": count}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
