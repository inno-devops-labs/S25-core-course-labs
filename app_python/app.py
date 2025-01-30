from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def get_time():
    msk_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(msk_timezone).strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Moscow Time</title>
    </head>
    <body>
        <h1>Current Time in Moscow:</h1>
        <p>{current_time}</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)