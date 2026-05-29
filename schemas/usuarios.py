from pydantic import BaseModel
from datetime import date

class UsuarioRegistro(BaseModel):
    nombre: str
    nombre_completo: str
    fecha_nacimiento: date
    password: str