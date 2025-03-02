import aiohttp
from fastapi import FastAPI
from router import router
from prometheus_fastapi_instrumentator import Instrumentator

session = None

app = FastAPI(title="Simple time application displaying time in Moscow")

instrumentator = Instrumentator().instrument(app)


@app.on_event("startup")
async def startup_event():
    instrumentator.expose(app)
    global session
    session = aiohttp.ClientSession()


@app.on_event("shutdown")
async def shutdown_event():
    await session.close()

app.include_router(router)
