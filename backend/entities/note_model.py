from typing import Union
from pydantic import BaseModel

class Note (BaseModel):
  id: int
  content: str
  