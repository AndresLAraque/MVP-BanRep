from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    rol = Column(String(20), nullable=False, default="empleado")
    created_at = Column(DateTime, default=datetime.utcnow)

    solicitudes = relationship("Solicitud", back_populates="empleado")
    aprobaciones = relationship("Aprobacion", back_populates="aprobador")


class Solicitud(Base):
    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True, index=True)
    empleado_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    destino = Column(String(200), nullable=False)
    pais = Column(String(100), nullable=False)
    motivo = Column(Text, nullable=False)
    fecha_inicio = Column(String(20), nullable=False)
    fecha_fin = Column(String(20), nullable=False)
    monto_total = Column(Float, nullable=False)
    anticipo = Column(Float, default=0.0)
    centro_costo = Column(String(150))
    estado = Column(String(30), nullable=False, default="borrador")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    empleado = relationship("Usuario", back_populates="solicitudes")
    detalles = relationship("DetalleGasto", back_populates="solicitud", cascade="all, delete-orphan")
    aprobaciones = relationship("Aprobacion", back_populates="solicitud", cascade="all, delete-orphan")
    documentos = relationship("Documento", back_populates="solicitud", cascade="all, delete-orphan")
    audit_log = relationship("AuditLog", back_populates="solicitud", cascade="all, delete-orphan",
                             order_by="AuditLog.timestamp")


class DetalleGasto(Base):
    __tablename__ = "detalle_gastos"

    id = Column(Integer, primary_key=True, index=True)
    solicitud_id = Column(Integer, ForeignKey("solicitudes.id"), nullable=False)
    categoria = Column(String(100), nullable=False)
    monto = Column(Float, nullable=False)
    descripcion = Column(String(300))

    solicitud = relationship("Solicitud", back_populates="detalles")


class Aprobacion(Base):
    __tablename__ = "aprobaciones"

    id = Column(Integer, primary_key=True, index=True)
    solicitud_id = Column(Integer, ForeignKey("solicitudes.id"), nullable=False)
    aprobador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nivel = Column(Integer, nullable=False)
    estado = Column(String(20), nullable=False, default="pendiente")
    comentario = Column(Text)
    fecha = Column(DateTime, default=datetime.utcnow)

    solicitud = relationship("Solicitud", back_populates="aprobaciones")
    aprobador = relationship("Usuario", back_populates="aprobaciones")


class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    solicitud_id = Column(Integer, ForeignKey("solicitudes.id"), nullable=False)
    nombre_archivo = Column(String(255), nullable=False)
    ruta_archivo = Column(String(500), nullable=False)
    tipo_mime = Column(String(100))
    ocr_texto = Column(Text)
    ocr_monto_detectado = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    solicitud = relationship("Solicitud", back_populates="documentos")


class AuditLog(Base):
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True, index=True)
    solicitud_id = Column(Integer, ForeignKey("solicitudes.id"), nullable=False)
    evento = Column(String(100), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    detalle = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    solicitud = relationship("Solicitud", back_populates="audit_log")
