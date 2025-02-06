from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/")
async def show_time():
    # Set the timezone to Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return {"message": f"The current time in Moscow is: {current_time}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
