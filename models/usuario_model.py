from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from typing import List

from core.configs import settings

from models.tarefa_model import TarefaModel

class UsuarioTarefaModel(settings.DBBaseModel):
    __tablename__ = 'usuario_tarefas'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    tarefa_id: Mapped[int] = Column('tarefa_id', ForeignKey('tarefas.id'))
    usuario_id: Mapped[int] = Column('usuario_id', ForeignKey('usuarios.id'))

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'
    
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String(256), nullable=True)
    sobrenome: Mapped[str] = Column(String(256), nullable=True)
    email: Mapped[str] = Column(String(256), index=True, nullable=False, unique=True)
    senha: Mapped[str] = Column(String(256), nullable=False)
    eh_admin: Mapped[bool] = Column(Boolean, default=False)
    tarefas: Mapped[List[UsuarioTarefaModel]] = relationship(
        "UsuarioTarefaModel",
        uselist=True
        # secondary='usuario_tarefas'
    )


                        
    
    