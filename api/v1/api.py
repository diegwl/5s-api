from fastapi import APIRouter

from api.v1.endpoints import tarefa, usuario, atribuirtarefas

api_router = APIRouter()

api_router.include_router(atribuirtarefas.router, prefix="/atribuir-tarefas", tags=['atribuir-tarefas'])
api_router.include_router(tarefa.router, prefix='/tarefas', tags=['tarefas'])
api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])