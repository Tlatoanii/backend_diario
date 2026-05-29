from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey, text
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


# ==========================================
# TABLA: USUARIOS
# ==========================================
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id_usuarios = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), unique=True, nullable=False)
    nombre_completo = Column(String(150), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    clave_secreta = Column(String(200), nullable=False)
    estado = Column(BIT(1), nullable=False, server_default=text("b'1'"))
    fecha_creacion = Column(DateTime, nullable=False, server_default=func.now())
    ultima_actualizacion = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    diarios = relationship("Diario", back_populates="propietario", cascade="all, delete-orphan")


# ==========================================
# TABLA: DIARIOS
# ==========================================
class Diario(Base):
    __tablename__ = "diarios"

    id_diario = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuarios"), primary_key=True, nullable=False)    
    fecha_redaccion = Column(Date, nullable=False)
    descripcion = Column(Text, nullable=False)
    estado = Column(BIT(1), nullable=False, server_default=text("b'1'"))
    fecha_creacion = Column(DateTime, nullable=False, server_default=func.now())
    ultima_modificacion = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    propietario = relationship("Usuario", back_populates="diarios")