"""
This module defines a simple FastAPI application with two endpoints:
1. The root endpoint ("/") that returns a welcome message.
2. An item endpoint ("/items/{item_id}") that returns details of a specific item.
Author: Sviatoslav Sviatkin (s.sviatkin@innopolis.university)
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    """
    Handle the root endpoint ("/").

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"Hello": "World"}


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: str):
    """
    Handle the endpoint for retrieving item details.

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        HTMLResponse: A HTML page containing the item ID.
    """
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": item_id}
    )
