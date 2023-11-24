from typing import Optional, List

from pydantic import BaseModel, EmailStr

from schemas.tarefa_schema import TarefaSchema

from schemas.usuario_tarefas_schema import UsuarioTarefaSchema

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        orm_mode = True
        
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    
class UsuarioSchemaTarefas(UsuarioSchemaBase):
    tarefas: Optional[List[UsuarioTarefaSchema]]
    
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]