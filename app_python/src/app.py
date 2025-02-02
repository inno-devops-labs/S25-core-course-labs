import uvicorn
from fastapi import FastAPI

from src.router import router
from src.settings import HOST, PORT

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("src.app:app", host=HOST, port=PORT, reload=False)
