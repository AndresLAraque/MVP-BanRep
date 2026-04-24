from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user

router = APIRouter(prefix="/solicitudes", tags=["solicitudes"])

ROLES_VEN_TODO = {"aprobador", "gh", "finanzas", "admin"}


def _log(db: Session, solicitud_id: int, evento: str, usuario_id: int, detalle: str = None):
    db.add(models.AuditLog(
        solicitud_id=solicitud_id,
        evento=evento,
        usuario_id=usuario_id,
        detalle=detalle,
        timestamp=datetime.utcnow(),
    ))


@router.post("", response_model=schemas.SolicitudOut, status_code=201)
def crear_solicitud(
    data: schemas.SolicitudCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = models.Solicitud(
        empleado_id=current_user.id,
        destino=data.destino,
        pais=data.pais,
        motivo=data.motivo,
        fecha_inicio=data.fecha_inicio,
        fecha_fin=data.fecha_fin,
        monto_total=data.monto_total,
        anticipo=data.anticipo,
        centro_costo=data.centro_costo,
        estado="pendiente",
    )
    db.add(sol)
    db.flush()

    for d in data.detalles:
        db.add(models.DetalleGasto(
            solicitud_id=sol.id,
            categoria=d.categoria,
            monto=d.monto,
            descripcion=d.descripcion,
        ))

    _log(db, sol.id, "SOLICITUD_CREADA", current_user.id,
         f"Destino: {sol.destino} | Monto: ${sol.monto_total:,.0f} COP")
    db.commit()
    db.refresh(sol)
    return sol


@router.get("", response_model=list[schemas.SolicitudOut])
def listar_solicitudes(
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    if current_user.rol in ROLES_VEN_TODO:
        return db.query(models.Solicitud).order_by(models.Solicitud.created_at.desc()).all()
    return (
        db.query(models.Solicitud)
        .filter(models.Solicitud.empleado_id == current_user.id)
        .order_by(models.Solicitud.created_at.desc())
        .all()
    )


@router.get("/{sol_id}", response_model=schemas.SolicitudOut)
def obtener_solicitud(
    sol_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == sol_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if current_user.rol == "empleado" and sol.empleado_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sin acceso a esta solicitud")
    return sol


@router.delete("/{sol_id}", status_code=204)
def eliminar_solicitud(
    sol_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == sol_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if sol.empleado_id != current_user.id and current_user.rol != "admin":
        raise HTTPException(status_code=403, detail="Sin permisos")
    db.delete(sol)
    db.commit()
