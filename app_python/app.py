import pytz
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Instrument the FastAPI app
instrumentator = Instrumentator()
instrumentator.instrument(app)
instrumentator.expose(app)

@app.get('/', response_class=HTMLResponse)
async def display_time(request: Request):
    try:
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
        return templates.TemplateResponse("index.html", {"request": request, "time": moscow_time})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/error', response_class=HTMLResponse)
async def handle_error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)