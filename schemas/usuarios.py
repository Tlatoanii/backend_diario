from pydantic import BaseModel
from datetime import date

class UsuarioRegistro(BaseModel):
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    password: str