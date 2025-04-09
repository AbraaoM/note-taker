from typing import Union
from pydantic import BaseModel

class Create_Note_DTO (BaseModel):
  content: str