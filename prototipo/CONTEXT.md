# Contexto — Prototipo Sistema de Viáticos
## Banco de la República · Dirección de Gestión Humana

---

## Propósito

Módulo de prueba independiente que implementa el núcleo del Sistema de Viáticos usando stack open source.
No afecta ni reemplaza la propuesta principal (Power Platform). Es coherente con su arquitectura, dominio y flujos.

**Objetivo**: tener una demo funcional, publicable, sin configuraciones complejas — `docker-compose up` y listo.

---

## Relación con el proyecto principal

| Aspecto | Proyecto principal | Este prototipo |
|---|---|---|
| Stack | Power Apps + Dataverse + Azure | FastAPI + PostgreSQL + HTML |
| Auth | Azure AD / Entra ID | JWT (Bearer) |
| Despliegue | Power Platform ambientes | Docker Compose |
| Dominio | Idéntico | Idéntico |
| Entidades | Idénticas | Idénticas |
| Flujo de aprobación | Idéntico | Idéntico |

---

## Stack

```
frontend/index.html  (HTML + CSS + JS puro)
        ↓  fetch()
backend/ FastAPI     (Python 3.11)
        ↓  SQLAlchemy ORM
PostgreSQL 16        (Docker)
        +
Tesseract OCR        (análisis de documentos adjuntos)
```

---

## Cómo ejecutar

### Requisitos
- Docker Desktop instalado y corriendo

### Levantar todo
```bash
cd prototipo
docker-compose up --build
```

### Abrir frontend
Abrir `frontend/index.html` directamente en el navegador (doble clic o `file://`).

La API estará en: http://localhost:8000  
Documentación interactiva: http://localhost:8000/docs

---

## Credenciales de prueba (cargadas automáticamente)

| Email | Password | Rol |
|---|---|---|
| carlos@banco.gov.co | demo1234 | empleado |
| maria@banco.gov.co | demo1234 | aprobador (Jefe) |
| ana@banco.gov.co | demo1234 | gh |
| finanzas@banco.gov.co | demo1234 | finanzas |
| admin@banco.gov.co | demo1234 | admin |

---

## Endpoints API

### Auth
| Método | Ruta | Descripción |
|---|---|---|
| POST | /auth/register | Registrar usuario |
| POST | /auth/login | Login → retorna JWT |

### Solicitudes
| Método | Ruta | Descripción |
|---|---|---|
| POST | /solicitudes | Crear solicitud |
| GET | /solicitudes | Listar (rol filtra: empleado ve las propias, aprobador ve todas) |
| GET | /solicitudes/{id} | Detalle + detalles de gasto |
| DELETE | /solicitudes/{id} | Eliminar borrador |

### Aprobaciones
| Método | Ruta | Descripción |
|---|---|---|
| POST | /aprobaciones/aprobar | Aprobar en nivel actual |
| POST | /aprobaciones/rechazar | Rechazar (comentario obligatorio) |

### Auditoría
| Método | Ruta | Descripción |
|---|---|---|
| GET | /auditoria/{solicitud_id} | Log completo de eventos |

### Documentos + OCR
| Método | Ruta | Descripción |
|---|---|---|
| POST | /documentos/{solicitud_id} | Subir archivo → extrae texto OCR + detecta monto |
| GET | /documentos/{solicitud_id} | Listar documentos con resultado OCR |

---

## Modelo de datos

```
Usuario        → id, nombre, email, password_hash, rol, created_at
Solicitud      → id, empleado_id, destino, pais, motivo, fecha_inicio, fecha_fin,
                 monto_total, anticipo, centro_costo, estado, created_at
DetalleGasto   → id, solicitud_id, categoria, monto, descripcion
Aprobacion     → id, solicitud_id, aprobador_id, nivel, estado, comentario, fecha
Documento      → id, solicitud_id, nombre_archivo, ruta, tipo_mime,
                 ocr_texto, ocr_monto_detectado, created_at
AuditLog       → id, solicitud_id, evento, usuario_id, detalle, timestamp
```

### Roles
`empleado` → `aprobador` (jefe) → `gh` → `finanzas` → `admin` (pagos)

### Estados de solicitud
`borrador` → `pendiente` → `en_aprobacion` → `aprobado` → `pagado` | `rechazado`

### Niveles de aprobación
1. Jefe directo (rol: `aprobador`)
2. Gestión Humana (rol: `gh`)
3. Presupuesto (rol: `finanzas`)
4. Compras (rol: `admin`)
5. Pago (rol: `admin`)

---

## OCR (Tesseract)

Al subir un documento (PDF, JPG, PNG):
1. Si es PDF: se convierte a imágenes con `pdf2image` (usa `poppler-utils`)
2. Se extrae texto con `pytesseract` en español (`lang=spa`)
3. Se buscan patrones de monto: `$1.200.000`, `TOTAL: 950000`, `VALOR COP`
4. El monto detectado se guarda en `ocr_monto_detectado` y se muestra en el frontend
5. Si Tesseract no está disponible, el sistema funciona igual sin OCR

---

## Sistema de diseño

| Token | Valor |
|---|---|
| Navy | `#002D72` |
| Gold | `#D4AF37` |
| Fuente | Segoe UI / system-ui |
| Estados badge | pending=gold, approved=green, draft=gray, paid=blue |

---

## Fases implementadas

- [x] FASE 1 — Backend base (FastAPI + PostgreSQL + modelos)
- [x] FASE 2 — Flujo de aprobaciones multinivel
- [x] FASE 3 — Frontend HTML conectado a API
- [x] FASE 4 — Auditoría y trazabilidad completa
- [x] FASE 5 — Upload de documentos (almacenamiento local)
- [x] FASE 6 — OCR con Tesseract (extracción de monto)
- [x] FASE 7 — JWT + roles + control de acceso

---

## Estructura de carpetas

```
prototipo/
├── CONTEXT.md                    ← este archivo
├── docker-compose.yml
├── Alternativa.txt               (referencia original)
├── prototipo_open_source.html    (referencia UI original)
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│       ├── auth.py
│       ├── solicitudes.py
│       ├── aprobaciones.py
│       ├── auditoria.py
│       └── documentos.py
│
└── frontend/
    └── index.html
```
