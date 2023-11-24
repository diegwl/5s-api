from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped, declarative_base

from models.tarefa_model import TarefaModel

from core.configs import settings

# class UsuarioTarefaModel(settings.DBBaseModel):
#     __tablename__ = 'usuario_tarefas'
#     __table_args__ = {'extend_existing': True}

#     id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
#     tarefa_id: Mapped[int] = Column('tarefa_id', ForeignKey('tarefas.id'))
#     usuario_id: Mapped[int] = Column('usuario_id', ForeignKey('usuarios.id'))