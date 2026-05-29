import os
from pathlib import Path
from fastapi import FastAPI, logger
from utils.logger import Logger
from routes.login import router as login_router
from routes.usuarios import router as usuarios_router

# Ruta del Logger, extraer la ruta completa con Path y luego crear la carpeta logs si no existe en la carpeta /logs
log_path = Path(os.path.join("logs", "app.log")).resolve()
log = Logger(log_path)

app = FastAPI(
    title="Api Diario Personal",
    description="Backend para el manejo de usuarios y entradas de diario",
    version="1.0.0"
)

log.logTitle("Diario")
log.logInfo("Inicializando la aplicación")

app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(login_router, tags=["Login"])

@app.get("/")
def read_root():
    log.logInfo("Accediendo a la ruta raíz")
    return {"message": "Bienvenido a la API del Diario Personal"}