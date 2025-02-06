from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import time_operations_router

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
