from fastapi import FastAPI
from app.routes.time_routes import router as time_router

app = FastAPI()

# Include the time router
app.include_router(time_router)


@app.get("/")
def read_root():
    return {"message": "Lab1 Moscow Time API"}
