from fastapi import APIRouter

from app.models.users import users
from app.utils.commons_database import insert
from app.utils.query_utils import insert_users

router = APIRouter()

@router.post("/usuarios")
def criar_usuario(usuario: users):

    insert(insert_users(usuario.nome_usuario,usuario.idade,usuario.genero,usuario.email,usuario.senha,usuario.id_tipo_usuario))
    return 'Sucesso!'

