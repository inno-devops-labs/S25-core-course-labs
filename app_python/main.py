from datetime import datetime
from zoneinfo import ZoneInfo   

from fastapi import FastAPI, Response

app = FastAPI()
zone = ZoneInfo('Europe/Moscow')

@app.get('/')
async def get_moscow_time() -> Response:
    time = datetime.now(zone).time()
    return Response(content=f'<h1>Moscow time: {time}</h1>')


@app.get('/visits')
async def inc_visit() -> Response:
    count = 0
    with open('visits') as f:
        line = f.readline()
        if line:
            count = int(line)
    
    count += 1
    with open('visits', 'w') as f:
        f.write(str(count))

    return Response(content=f'visitors: {count}')