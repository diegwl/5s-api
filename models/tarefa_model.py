from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from core.configs import settings

class TarefaModel(settings.DBBaseModel):
    __tablename__ = 'tarefas'
    
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = Column(String(256))
