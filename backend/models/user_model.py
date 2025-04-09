from typing import Union
from pydantic import BaseModel

class User (BaseModel):
  id: int
  name: str
  avatar_url: str
  