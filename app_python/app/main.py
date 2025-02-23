from fastapi import FastAPI
from routers.time import router as TimeRouter

app = FastAPI()
app.include_router(TimeRouter)