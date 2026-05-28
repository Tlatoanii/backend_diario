from fastapi import FastAPI

app = FastAPI(
    title="Api Diario Personal",
    description="Backend para el manejo de usuarios y entradas de diario",
    version="1.0.0"
)

DATABASE_URL = "mysql+pymysql://root:tu_contraseña@localhost:3306/DB_Diario"

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Diario Personal"}