from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    rol: str = "empleado"


class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: str
    rol: str
    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UsuarioOut


class DetalleGastoCreate(BaseModel):
    categoria: str
    monto: float
    descripcion: Optional[str] = None


class DetalleGastoOut(DetalleGastoCreate):
    id: int
    model_config = {"from_attributes": True}


class SolicitudCreate(BaseModel):
    destino: str
    pais: str
    motivo: str
    fecha_inicio: str
    fecha_fin: str
    monto_total: float
    anticipo: float = 0.0
    centro_costo: Optional[str] = None
    detalles: list[DetalleGastoCreate] = []


class SolicitudOut(BaseModel):
    id: int
    destino: str
    pais: str
    motivo: str
    fecha_inicio: str
    fecha_fin: str
    monto_total: float
    anticipo: float
    centro_costo: Optional[str]
    estado: str
    created_at: datetime
    empleado: UsuarioOut
    detalles: list[DetalleGastoOut] = []
    model_config = {"from_attributes": True}


class AprobacionCreate(BaseModel):
    solicitud_id: int
    comentario: Optional[str] = None


class AprobacionOut(BaseModel):
    id: int
    nivel: int
    estado: str
    comentario: Optional[str]
    fecha: datetime
    aprobador: UsuarioOut
    model_config = {"from_attributes": True}


class AuditLogOut(BaseModel):
    id: int
    evento: str
    detalle: Optional[str]
    timestamp: datetime
    model_config = {"from_attributes": True}


class DocumentoOut(BaseModel):
    id: int
    nombre_archivo: str
    tipo_mime: Optional[str]
    ocr_texto: Optional[str]
    ocr_monto_detectado: Optional[float]
    created_at: datetime
    model_config = {"from_attributes": True}
