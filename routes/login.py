import os
from pathlib import Path
from database import get_db
from utils.logger import Logger
from models.models import Usuario
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, Depends, status
from utils.security import verify_password, create_access_token

router = APIRouter()

#==========================================
# Crear logger para esta ruta misma que se usará en main.py, extraer la ruta completa con Path y luego crear la carpeta logs si no existe en la carpeta /logs
#==========================================
log_path = Path(os.path.join("logs", "app.log")).resolve()
log = Logger(log_path)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.nombre == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(form_data.password, user.clave_secreta):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.id_usuarios})
    log.logInfo(f"Usuario autenticado: {user.id_usuarios}")
    return {"access_token": access_token, "token_type": "bearer"}