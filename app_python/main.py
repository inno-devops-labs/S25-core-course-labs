import uvicorn
from fastapi import FastAPI

from settings import APP_HOST, APP_PORT
from routes import time_router, visits_router
from prometheus_fastapi_instrumentator import Instrumentator


def main() -> None:
    app = FastAPI()
    app.include_router(time_router)
    app.include_router(visits_router)

    Instrumentator().instrument(app).expose(app)

    uvicorn.run(app, host=APP_HOST, port=APP_PORT)


if __name__ == "__main__":
    main()
