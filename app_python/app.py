import uvicorn
from fastapi import FastAPI

from settings import HOST, PORT
from router import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=PORT, reload=False)