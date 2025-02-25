from fastapi import FastAPI
from routes import index
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app, endpoint="/metrics")

app.include_router(index.router)

if __name__ == '__main__':
    import uvicorn
    from utils.config import Config
    uvicorn.run(
        "main:app",
        host=Config.APP_HOST,
        port=Config.APP_PORT,
        log_level="info",
        reload=True
    )
