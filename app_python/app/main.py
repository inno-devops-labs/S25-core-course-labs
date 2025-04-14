from fastapi import FastAPI
from routes import index

app = FastAPI()

app.include_router(index.router)

if __name__ == '__main__':
    import uvicorn
    from config import settings
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        log_level="info",
        reload=True
    )
