from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.tarefa_model import TarefaModel
from models.usuario_model import UsuarioModel
from schemas.tarefa_schema import TarefaSchema
from core.deps import get_session, get_current_user

router = APIRouter()

# POST Tarefa
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TarefaSchema)
async def post_artigo(artigo: TarefaSchema, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
   if usuario_logado.eh_admin == True:
    novo_artigo: TarefaModel = TarefaModel(titulo=artigo.titulo)
    
    db.add(novo_artigo)
    await db.commit()
    
    return novo_artigo
   else:
        raise HTTPException(detail='Não autorizado', status_code=status.HTTP_401_UNAUTHORIZED)

# GET Tarefas
@router.get('/', response_model=List[TarefaSchema])
async def get_artigos(db: AsyncSession = Depends(get_session)):
     async with db as session:
         query = select(TarefaModel)
         result = await session.execute(query)
         artigos: List[TarefaModel] = result.scalars().unique().all()
         
         return artigos
     
# GET Tarefa
@router.get('/{artigo_id}', response_model=TarefaSchema, status_code=status.HTTP_200_OK)
async def get_artigo(artigo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.id == artigo_id)
        result = await session.execute(query)
        artigo: TarefaModel = result.scalars().unique().one_or_none()
        
        if artigo:
            return artigo
        else:
            raise HTTPException(detail='Artigo não encontrado', status_code=status.HTTP_404_NOT_FOUND)