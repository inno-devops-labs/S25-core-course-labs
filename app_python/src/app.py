from fastapi import FastAPI
from src.routes import ALL_ROUTERS

app = FastAPI()

for router in ALL_ROUTERS:
    app.include_router(router)
