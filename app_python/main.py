import os
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import time_operations_router
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

load_dotenv()  # Load environmental variables
COUNTER_FILE = os.getenv("COUNTER_FILE", "data/visits.txt")

# 1. Make sure the directory for COUNTER_FILE exists
os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)

# 2. Ensure the file itself exists
if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        f.write("0")

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

# Define the root resource
@app.get("/")
def root():
    # Read the current counter
    with open(COUNTER_FILE, "r") as f:
        count = int(f.read().strip())

    # Increment and save
    count += 1
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))

    return {"message": f"Hello! You are visitor #{count}."}

@app.get("/visits")
def get_visits():
    with open(COUNTER_FILE, "r") as f:
        count = f.read().strip()
    return {"total_visits": count}

# Define the metrics endpoint
@app.get("/metrics")
def metrics():
    # generate_latest() returns the latest metrics in Prometheus text format
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
