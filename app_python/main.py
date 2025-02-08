import aiohttp
from fastapi import FastAPI
from router import router

session = None

app = FastAPI(title="Simple time application displaying time in Moscow")


@app.on_event("startup")
async def startup_event():
    global session
    session = aiohttp.ClientSession()


@app.on_event("shutdown")
async def shutdown_event():
    await session.close()

app.include_router(router)
