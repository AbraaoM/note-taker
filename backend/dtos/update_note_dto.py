from typing import Union
from pydantic import BaseModel

class Update_Note_DTO (BaseModel):
  id: int
  content: str