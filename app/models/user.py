from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    height: float
    weight: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "張三",
                "height": 175.5,
                "weight": 65.0
            }
        }