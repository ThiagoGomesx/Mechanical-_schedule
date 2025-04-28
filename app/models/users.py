from pydantic import BaseModel
class users(BaseModel):

    nome_usuario: str
    idade: int
    genero: str
    email: str
    senha: str
    id_tipo_usuario: int

