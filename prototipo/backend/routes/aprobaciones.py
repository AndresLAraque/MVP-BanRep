from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user

router = APIRouter(prefix="/aprobaciones", tags=["aprobaciones"])

# Rol requerido por nivel de aprobación
NIVEL_ROL = {
    1: "aprobador",   # Jefe directo
    2: "gh",          # Gestión Humana
    3: "finanzas",    # Presupuesto
    4: "admin",       # Compras
    5: "admin",       # Pago
}
MAX_NIVELES = 5

ESTADOS_FINALES = {"aprobado", "rechazado", "pagado"}


def _log(db, solicitud_id, evento, usuario_id, detalle=None):
    db.add(models.AuditLog(
        solicitud_id=solicitud_id,
        evento=evento,
        usuario_id=usuario_id,
        detalle=detalle,
        timestamp=datetime.utcnow(),
    ))


def _nivel_siguiente(sol: models.Solicitud) -> int:
    aprobados = [a for a in sol.aprobaciones if a.estado == "aprobado"]
    return len(aprobados) + 1


@router.post("/aprobar")
def aprobar(
    data: schemas.AprobacionCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == data.solicitud_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if sol.estado in ESTADOS_FINALES:
        raise HTTPException(status_code=400, detail=f"Solicitud ya está en estado '{sol.estado}'")

    nivel = _nivel_siguiente(sol)
    rol_requerido = NIVEL_ROL.get(nivel)

    if current_user.rol != "admin" and current_user.rol != rol_requerido:
        raise HTTPException(
            status_code=403,
            detail=f"Nivel {nivel} requiere rol '{rol_requerido}'. Tu rol es '{current_user.rol}'"
        )

    db.add(models.Aprobacion(
        solicitud_id=sol.id,
        aprobador_id=current_user.id,
        nivel=nivel,
        estado="aprobado",
        comentario=data.comentario,
    ))

    if nivel >= MAX_NIVELES:
        sol.estado = "aprobado"
        evento = "APROBADO_FINAL"
        detalle = "Todos los niveles completados — listo para pago"
    else:
        sol.estado = "en_aprobacion"
        nivel_nombres = {1: "Jefe", 2: "GH", 3: "Presupuesto", 4: "Compras", 5: "Pago"}
        evento = f"APROBADO_NIVEL_{nivel}_{nivel_nombres.get(nivel, nivel)}"
        detalle = data.comentario

    _log(db, sol.id, evento, current_user.id, detalle)
    db.commit()

    return {
        "mensaje": f"Aprobado en nivel {nivel}",
        "nuevo_estado": sol.estado,
        "nivel_completado": nivel,
        "siguiente_nivel": nivel + 1 if nivel < MAX_NIVELES else None,
    }


@router.post("/rechazar")
def rechazar(
    data: schemas.AprobacionCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == data.solicitud_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if sol.estado in ESTADOS_FINALES:
        raise HTTPException(status_code=400, detail=f"Solicitud ya en estado '{sol.estado}'")
    if not data.comentario or not data.comentario.strip():
        raise HTTPException(status_code=400, detail="El motivo de rechazo es obligatorio")

    nivel = _nivel_siguiente(sol)
    db.add(models.Aprobacion(
        solicitud_id=sol.id,
        aprobador_id=current_user.id,
        nivel=nivel,
        estado="rechazado",
        comentario=data.comentario,
    ))
    sol.estado = "rechazado"
    _log(db, sol.id, "RECHAZADO", current_user.id, data.comentario)
    db.commit()

    return {"mensaje": "Solicitud rechazada", "nuevo_estado": sol.estado}


@router.get("/{solicitud_id}", response_model=list[schemas.AprobacionOut])
def listar_aprobaciones(
    solicitud_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return sol.aprobaciones
