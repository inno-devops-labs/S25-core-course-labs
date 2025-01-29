"""
Module containing Pydantic models for the web application.
"""

from pydantic import BaseModel


class Time(BaseModel):
    """Basic time model."""

    time: str
