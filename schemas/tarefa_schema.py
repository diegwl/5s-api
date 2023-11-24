from typing import Optional

from pydantic import BaseModel, HttpUrl

class TarefaSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    
    class Config:
        orm_mode = True