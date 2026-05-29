import os
from pathlib import Path
from database import get_db
from utils.logger import Logger
from models.models import Usuario
from sqlalchemy.orm import Session
from utils.security import get_password_hash
from schemas.usuarios import UsuarioRegistro
from fastapi import APIRouter, Depends, HTTPException, status

#==========================================
# Crear logger para esta ruta misma que se usará en main.py, extraer la ruta completa con Path y luego crear la carpeta logs si no existe en la carpeta /logs
#==========================================
log_path = Path(os.path.join("logs", "app.log")).resolve()
log = Logger(log_path)


#==========================================
# RUTA: /usuarios/registro
#==========================================
router = APIRouter()
@router.post("/registro", status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario_in: UsuarioRegistro, db: Session = Depends(get_db)):
    log.logInfo(f"Intentando registrar usuario: {usuario_in.nombre} {usuario_in.nombre_completo} con fecha de nacimiento {usuario_in.fecha_nacimiento} y password de longitud {len(usuario_in.password)} caracteres ({len(usuario_in.password.encode('utf-8'))} bytes)")
    try: 
        usuario_repetido = db.query(Usuario).filter(Usuario.nombre == usuario_in.nombre).first()
        if usuario_repetido:
            log.logWarning(f"Intento de registro con nombre de usuario repetido: {usuario_in.nombre}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de usuario ya está en uso")
        
        hash_password = get_password_hash(usuario_in.password)
        nuevo_usuario = Usuario(
            nombre=usuario_in.nombre,
            nombre_completo=usuario_in.nombre_completo,
            fecha_nacimiento=usuario_in.fecha_nacimiento,
            clave_secreta=hash_password
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        log.logInfo(f"Usuario registrado: {nuevo_usuario.id_usuarios}")
        return {"message": "Usuario registrado exitosamente", "usuario_id": nuevo_usuario.id_usuarios}
    except Exception as e:
        db.rollback()
        log.logError(f"Error al registrar el usuario {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al registrar el usuario {str(e)}")