from fastapi import FastAPI
from routes import index

app = FastAPI()

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
