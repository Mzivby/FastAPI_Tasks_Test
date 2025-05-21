from typing import Optional
from pydantic import BaseModel



class TaskAddSchema(BaseModel):
    name: str
    description: Optional[str] = None

class TaskSchema(TaskAddSchema):
    id: int


