"""
 In this module we implement a simplistic web service that provides
 current time in Moscow.

 SPDX-LICENCE: no-licence
 Author: Elon Max
"""

from fastapi import FastAPI
from routers import time_router

app = FastAPI()

# Include the router from the time module
app.include_router(time_router)
