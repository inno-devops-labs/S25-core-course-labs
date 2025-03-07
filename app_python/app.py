from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz
from prometheus_fastapi_instrumentator import Instrumentator
import os

app = FastAPI()

VISITS_FILE = "/app/visits.txt"

Instrumentator().instrument(app).expose(app)

def increment_visit() -> int:
  os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)

  count = 0
  if os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "r") as f:
      count = int(f.read())
  
  count += 1
  with open(VISITS_FILE, "w") as f:
      f.write(str(count))
  
  return count

@app.get("/", response_class=HTMLResponse)
async def get_moscow_time():
  increment_visit()
  moscow_tz = pytz.timezone("Europe/Moscow")
  current_time = datetime.now(moscow_tz).strftime("%H:%M:%S").split(":")

  html_content = f"""
  <html>
      <head>
          <title>Текущее Московское время</title>
      </head>
      <body style="display: flex; justify-content: center; background: #222">
          <div style="display: inline-flex; justify-content: center;">
            <p style="font-size: 154px; color: #fbcb40; margin: 0;">
              {current_time[0]}:{current_time[1]}
            </p>
            <p style="color: white; font-size: 72px; margin: 15px 0 0 0;">
              {current_time[2]}
            </p>
          </div>
      </body>
  </html>
  """

  return HTMLResponse(content=html_content)

@app.get("/visits")
async def visits():
  if os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "r") as f:
      count = int(f.read())

  return f"Total Visits: {count}"