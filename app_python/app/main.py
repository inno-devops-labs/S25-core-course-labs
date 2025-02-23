from fastapi import FastAPI
from routers.time import router as TimeRouter
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
app.include_router(TimeRouter)

@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)