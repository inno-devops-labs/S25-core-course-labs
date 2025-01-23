"""
This module defines a simple FastAPI application with two endpoints:
1. The root endpoint ("/") that returns a welcome message.
2. An item endpoint ("/items/{item_id}") that returns details of a specific item.
Author: Sviatoslav Sviatkin (s.sviatkin@innopolis.university)
"""

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    Handle the root endpoint ("/").

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Handle the endpoint for retrieving item details.

    Args:
        item_id (int): The ID of the item to retrieve.
        q (Union[str, None], optional): An optional query parameter.

    Returns:
        dict: A dictionary containing the item ID and the optional query parameter.
    """
    return {"item_id": item_id, "q": q}
