import os
import re
import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

MIME_PERMITIDOS = {
    "application/pdf",
    "image/jpeg",
    "image/png",
    "image/jpg",
}

# Intentar importar dependencias OCR — el sistema funciona sin ellas
try:
    import pytesseract
    from PIL import Image
    import pdf2image
    OCR_DISPONIBLE = True
except ImportError:
    OCR_DISPONIBLE = False

router = APIRouter(prefix="/documentos", tags=["documentos"])


def _extraer_ocr(ruta: str, tipo_mime: str) -> str:
    if not OCR_DISPONIBLE:
        return ""
    try:
        if tipo_mime == "application/pdf":
            paginas = pdf2image.convert_from_path(ruta, dpi=200)
            return "\n".join(
                pytesseract.image_to_string(p, lang="spa") for p in paginas
            ).strip()
        else:
            img = Image.open(ruta)
            return pytesseract.image_to_string(img, lang="spa").strip()
    except Exception:
        return ""


def _detectar_monto(texto: str) -> float | None:
    """
    Busca patrones de monto en texto OCR extraído de facturas colombianas.
    Formatos esperados: $1.200.000, TOTAL: 950000, VALOR COP 2500000
    """
    patrones = [
        r'TOTAL[\s:$]*([\d.,]+)',
        r'VALOR[\s:$]*([\d.,]+)',
        r'\$\s*([\d.,]+)',
        r'([\d.,]+)\s*COP',
        r'SUBTOTAL[\s:$]*([\d.,]+)',
    ]
    for patron in patrones:
        match = re.search(patron, texto, re.IGNORECASE)
        if match:
            raw = match.group(1).replace('.', '').replace(',', '.')
            try:
                valor = float(raw)
                if valor > 0:
                    return valor
            except ValueError:
                continue
    return None


@router.post("/{solicitud_id}", response_model=schemas.DocumentoOut, status_code=201)
async def subir_documento(
    solicitud_id: int,
    archivo: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if current_user.rol == "empleado" and sol.empleado_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sin acceso a esta solicitud")
    if archivo.content_type not in MIME_PERMITIDOS:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido. Use PDF, JPG o PNG.")

    ext = os.path.splitext(archivo.filename or "doc")[1] or ".bin"
    nombre_guardado = f"{uuid.uuid4().hex}{ext}"
    ruta = os.path.join(UPLOAD_DIR, nombre_guardado)

    contenido = await archivo.read()
    with open(ruta, "wb") as f:
        f.write(contenido)

    texto_ocr = _extraer_ocr(ruta, archivo.content_type)
    monto_detectado = _detectar_monto(texto_ocr) if texto_ocr else None

    doc = models.Documento(
        solicitud_id=solicitud_id,
        nombre_archivo=archivo.filename,
        ruta_archivo=ruta,
        tipo_mime=archivo.content_type,
        ocr_texto=texto_ocr or None,
        ocr_monto_detectado=monto_detectado,
    )
    db.add(doc)
    db.add(models.AuditLog(
        solicitud_id=solicitud_id,
        evento="DOCUMENTO_SUBIDO",
        usuario_id=current_user.id,
        detalle=(
            f"{archivo.filename} | "
            f"OCR: {'activo' if texto_ocr else 'sin texto'} | "
            f"Monto detectado: ${monto_detectado:,.0f}" if monto_detectado else f"{archivo.filename} | OCR sin monto"
        ),
        timestamp=datetime.utcnow(),
    ))
    db.commit()
    db.refresh(doc)
    return doc


@router.get("/{solicitud_id}", response_model=list[schemas.DocumentoOut])
def listar_documentos(
    solicitud_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user),
):
    sol = db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()
    if not sol:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    if current_user.rol == "empleado" and sol.empleado_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sin acceso")
    return sol.documentos
