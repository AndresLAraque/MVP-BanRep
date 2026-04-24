import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models
from auth import hash_password
from routes import auth, solicitudes, aprobaciones, auditoria, documentos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Viáticos — Banco de la República",
    description="API REST para gestión de solicitudes de viáticos · Prototipo open source",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(solicitudes.router)
app.include_router(aprobaciones.router)
app.include_router(auditoria.router)
app.include_router(documentos.router)


# ── Seed: usuarios de demo ──────────────────────────────────────────────────

DEMO_USERS = [
    {"nombre": "Carlos Mejía",    "email": "carlos@banco.gov.co",   "password": "demo1234", "rol": "empleado"},
    {"nombre": "María Rodríguez", "email": "maria@banco.gov.co",    "password": "demo1234", "rol": "aprobador"},
    {"nombre": "Ana Torres",      "email": "ana@banco.gov.co",      "password": "demo1234", "rol": "gh"},
    {"nombre": "Luis Financiero", "email": "finanzas@banco.gov.co", "password": "demo1234", "rol": "finanzas"},
    {"nombre": "Admin Sistema",   "email": "admin@banco.gov.co",    "password": "demo1234", "rol": "admin"},
]


@app.on_event("startup")
def seed_demo_users():
    db: Session = SessionLocal()
    try:
        for u in DEMO_USERS:
            exists = db.query(models.Usuario).filter(models.Usuario.email == u["email"]).first()
            if not exists:
                db.add(models.Usuario(
                    nombre=u["nombre"],
                    email=u["email"],
                    password_hash=hash_password(u["password"]),
                    rol=u["rol"],
                ))
        db.commit()
    finally:
        db.close()


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


# Sirve el frontend como archivos estáticos (solo en producción, cuando existe /app/static)
_static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
if os.path.exists(_static_dir):
    app.mount("/", StaticFiles(directory=_static_dir, html=True), name="frontend")
