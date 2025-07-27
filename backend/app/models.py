# models.py - Data models and schemas

from pydantic import BaseModel

class TripRequest(BaseModel):
    destination: str
    dates: str
    budget: float
