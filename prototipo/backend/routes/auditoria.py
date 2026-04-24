from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user

router = APIRouter(prefix="/auditoria", tags=["auditoria"])


@router.get("/{solicitud_id}", response_model=list[schemas.AuditLogOut])
def obtener_auditoria(
    solicitud_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if current_user.rol == "empleado" and sol.empleado_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sin acceso")
    return sol.audit_log
