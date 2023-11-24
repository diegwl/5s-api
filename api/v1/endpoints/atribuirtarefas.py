from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from random import randint

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.tarefa_model import TarefaModel
from models.usuario_model import UsuarioModel
from schemas.tarefa_schema import TarefaSchema
from schemas.usuario_tarefas_schema import UsuarioTarefaSchema
from core.deps import get_session, get_current_user

from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchemaBase, UsuarioSchemaCreate, UsuarioSchemaUp, UsuarioSchemaTarefas

from models.usuario_model import UsuarioTarefaModel

router = APIRouter()

# POST Atribuir Tarefas
@router.post('/', status_code=status.HTTP_201_CREATED)
async def atribuir_tarefas(usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
   if usuario_logado.eh_admin == True:
      query = select(UsuarioModel)
      result = await db.execute(query)
      usuarios: List[UsuarioSchemaBase] = result.scalars().unique().all()

      query2 = select(TarefaModel)
      result2 = await db.execute(query2)
      tarefas: List[TarefaSchema] = result2.scalars().unique().all()

      sorteados = []

      for usuario in usuarios:
         if usuario.eh_admin:
            pass
         else:
            while True:
               num = randint(0, len(tarefas)-1)
      
               if num not in sorteados:
                  sorteados.append(num)
                  new: UsuarioTarefaModel = UsuarioTarefaModel(usuario_id=usuario.id, tarefa_id=tarefas[num].id)

                  db.add(new)
                  break
               
               elif len(sorteados) == len(tarefas):
                  sorteados = []
      
      await db.commit()
   else:
        raise HTTPException(detail='Não autorizado', status_code=status.HTTP_401_UNAUTHORIZED)
