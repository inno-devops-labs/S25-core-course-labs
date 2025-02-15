from datetime import datetime
from zoneinfo import ZoneInfo   

from fastapi import FastAPI, Response

app = FastAPI()
zone = ZoneInfo('Europe/Moscow')

@app.get('/')
async def get_moscow_time() -> Response:
    time = datetime.now(zone).time()
    return Response(content=f'<h1>Moscow time: {time}</h1>')