# Plan de Implementacion -- MVP Sistema de Viaticos

## Banco de la Republica - Direccion de Gestion Humana

---

## 1. Objetivo

Digitalizar el proceso de solicitud, aprobacion, pago y trazabilidad de viaticos para equipos que viajan a organizaciones nacionales e internacionales a conocer implementaciones de IA. El MVP reemplaza el flujo manual (correo + Excel) por una solucion en Power Platform con cumplimiento del Art. 130 del Codigo Sustantivo del Trabajo.

---

## 2. Decisiones Confirmadas

| Decision | Definicion |
|----------|-----------|
| Idioma | Espanol (es-CO) |
| Migracion SAP | Brownfield: preserva configuracion y datos historicos |
| Integracion SAP | OData Services (REST/JSON) simulados en Dataverse, estructura identica a S/4HANA para reemplazo directo posterior |
| Mapeo identidad | Azure AD (email corporativo) se mapea a PERNR de SAP via tabla de empleados |
| Topes de monto | Configurables por administrador, no varian por cargo. Valores iniciales aproximados con fuentes reales |
| Tarjetas corporativas | Se simula el pago por tarjeta y el proceso de conciliacion contra extracto bancario |
| Plataforma de datos | Dataverse real (Developer Plan free tier) |
| DevOps | Azure DevOps Free Tier (5 usuarios, repos ilimitados, 1 pipeline) |
| Marco legal | Art. 130 CST con discriminacion obligatoria por categoria de gasto |
| Documentos | Columnas de archivo en Dataverse (sin SharePoint en demo) |

---

## 3. Estrategia de Licenciamiento Gratuito

| Componente | Plan | Costo |
|-----------|------|-------|
| Power Apps | Developer Plan | $0 |
| Power Automate | Incluido en Developer Plan | $0 |
| Dataverse | Incluido en Developer Plan | $0 |
| Azure DevOps | Free Tier (5 usuarios Basic) | $0 |
| Correo | Conector Outlook o SMTP gratuito | $0 |

Requisito: cuenta de trabajo o escuela respaldada por Microsoft Entra ID.

Ruta de escalamiento: Developer Plan (demo) -> Power Apps per-app ($5 USD/usuario/mes) -> Power Apps per-user ($20 USD/usuario/mes).

---

## 4. Resumen de Componentes

La documentacion detallada de cada componente se encuentra en los archivos referenciados:

| Componente | Documento de referencia |
|-----------|----------------------|
| Flujo AS-IS y TO-BE | [02_propuesta_proceso.md](02_propuesta_proceso.md) |
| Arquitectura, RBAC y DevOps | [03_arquitectura.md](03_arquitectura.md) |
| Modelo de datos, estados, SAP simulado y topes | [04_modelo_datos.md](04_modelo_datos.md) |
| Marco legal Art. 130 CST | [05_marco_legal.md](05_marco_legal.md) |
| Historias de usuario con criterios de aceptacion | [06_historias_usuario.md](06_historias_usuario.md) |
| Backlog por modulo | [07_backlog.md](07_backlog.md) |
| Cronograma, tareas y pruebas | [08_cronograma.md](08_cronograma.md) |
| Plan de pruebas y casos de prueba | [09_plan_pruebas.md](09_plan_pruebas.md) |
| Gobernanza de datos y DLP | [10_gobernanza_datos.md](10_gobernanza_datos.md) |
| Plan de capacitacion por rol | [11_plan_capacitacion.md](11_plan_capacitacion.md) |
| SRE, seguridad y operaciones | [12_sre_seguridad.md](12_sre_seguridad.md) |
| Registro de riesgos y contingencia | [13_riesgos.md](13_riesgos.md) |
| Costos y presupuesto del proyecto | [14_costos_presupuesto.md](14_costos_presupuesto.md) |
| Viabilidad y analisis costo-beneficio | [15_viabilidad_costo_beneficio.md](15_viabilidad_costo_beneficio.md) |

---

## 5. Cronograma Resumido

| Fase | Semana | Foco | Entregable |
|------|--------|------|-----------|
| Descubrimiento | S1 | Reglas de negocio, topes, contrato SAP, setup Azure DevOps | Backlog en Boards, reglas parametrizadas |
| Arquitectura | S2 | Tablas Dataverse, RBAC, tablas SAP simuladas, pipeline base | Ambiente Dev configurado |
| Sprint 1 | S3 | HU-01,03,04,05,12,13,14,18 | Formulario + aprobacion N1 + notificaciones |
| Sprint 2 | S4 | HU-06,07,08,09,10 | MVP E2E funcional |
| Pruebas | S5 | Funcional, integracion, RBAC, UAT | MVP validado |
| Despliegue | S6 | Pipeline Prod, grupo piloto, capacitacion | Sistema en produccion |
| Estabilizacion | S7 | HU-02,11,15 + monitoreo + ajustes | Sistema estable |
| Mejoras | S8 | OCR piloto, Dashboard, integracion SAP real | Extensiones |

Detalle completo en [08_cronograma.md](08_cronograma.md).

---

## 6. Estructura del Repositorio

```
MVP/
|-- README.md
|-- docs/
|   |-- 01_plan_implementacion.md
|   |-- 02_propuesta_proceso.md
|   |-- 03_arquitectura.md
|   |-- 04_modelo_datos.md
|   |-- 05_marco_legal.md
|   |-- 06_historias_usuario.md
|   |-- 07_backlog.md
|   |-- 08_cronograma.md
|   |-- 09_plan_pruebas.md
|   |-- 10_gobernanza_datos.md
|   |-- 11_plan_capacitacion.md
|   |-- 12_sre_seguridad.md
|   |-- 13_riesgos.md
|   |-- 14_costos_presupuesto.md
|   |-- 15_viabilidad_costo_beneficio.md
|
|-- solucion/
|   |-- dataverse/
|   |   |-- tablas/
|   |   |-- reglas/
|   |   |-- roles/
|   |   |-- configuracion/
|   |   |-- sap_simulado/
|   |-- power_apps/
|   |-- power_automate/
|   |   |-- flujo_solicitud/
|   |   |-- flujo_aprobacion/
|   |   |-- flujo_pago/
|   |   |-- flujo_notificaciones/
|   |   |-- flujo_auditoria/
|
|-- pruebas/
|   |-- casos/
|   |-- evidencias/
|   |-- uat/
|
|-- despliegue/
    |-- pipelines/
```

---

## 7. Verificacion

| Sprint | Tipo | Verificacion |
|--------|------|-------------|
| Sprint 1 | Funcional | Solicitud con desglose legal, aprobacion N1, notificaciones, RBAC |
| Sprint 2 | Integracion | Flujo E2E hasta pago simulado en tablas SAP |
| Pruebas | UAT | Usuarios reales de GH, permisos por rol |
| Despliegue | Smoke | Pipeline DevOps import + verificacion |

| Metrica | Objetivo |
|---------|----------|
| Solicitudes sin error | >= 95% |
| Tiempo aprobacion por nivel | < 48h |
| Clasificacion legal correcta | 100% |
| Pipeline DevOps exitoso | >= 90% |
| Satisfaccion UAT | >= 4/5 |
