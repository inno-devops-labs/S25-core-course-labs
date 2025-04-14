import uvicorn
from fastapi import FastAPI

from settings import APP_HOST, APP_PORT
from routes import router


def main() -> None:
    app = FastAPI(
            prefix="/api/v1"
    )
    app.include_router(router)

    uvicorn.run(app, host=APP_HOST, port=APP_PORT)


if __name__ == "__main__":
    main()
