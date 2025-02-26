from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import time_operations_router

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST


load_dotenv()  # Load environmental variables

# Create the backend application
app = FastAPI()

# Allow all origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the routers
app.include_router(time_operations_router)


# Define the root source
@app.get("/", tags=["Root"], status_code=200)
async def root():
    return {"message": "The python application is up!"}

# Define the metrics endpoint
@app.get("/metrics")
def metrics():
    # generate_latest() returns the latest metrics in Prometheus text format
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
