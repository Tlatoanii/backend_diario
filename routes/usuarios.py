from database import get_db
from utils.logger import Logger
from models.models import Usuario
from sqlalchemy.orm import Session
from utils.security import get_password_hash
from schemas.usuarios import UsuarioRegistro
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

@router.post("/registro", status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario_in: UsuarioRegistro, db: Session = Depends(get_db)):
    hash_password = get_password_hash(usuario_in.password)
    nuevo_usuario = Usuario(
        nombre=usuario_in.nombre,
        apellidos=usuario_in.apellidos,
        fecha_nacimiento=usuario_in.fecha_nacimiento,
        clave_secreta=hash_password
    )
    try: 
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        
        return {"message": "Usuario registrado exitosamente", "usuario_id": nuevo_usuario.id_usuarios}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al registrar el usuario {str(e)}")