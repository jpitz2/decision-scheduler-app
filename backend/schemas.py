# Defines the shape of incoming data requests

from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    name:str
    priority:str
    duration: Optional[int] = None
    completion_status:bool = False