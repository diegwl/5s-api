from typing import Optional

from pydantic import BaseModel, HttpUrl

class UsuarioTarefaSchema(BaseModel):
    id: int
    usuario_id: int
    tarefa_id: int
    
    class Config:
        orm_mode = True