# Cronograma de Implementacion - 8 Semanas

## Enfoque

- Metodologia: Agil (sprints semanales)
- Entrega MVP: Semana 4
- Estabilizacion y mejoras: Semanas 5-8
- Gestion de trabajo: Azure DevOps Boards
- Despliegue: Azure DevOps Pipelines

---

## Fase 1: Descubrimiento y Definicion (Semana 1)

### Objetivo
Entender el proceso, definir alcance, construir backlog y configurar herramientas.

### Tareas

| Tarea | Responsable | Entregable |
|-------|-------------|-----------|
| Kickoff con stakeholders (GH, Finanzas, TI) | Product Owner | Acta de inicio |
| Levantamiento del proceso AS-IS | Analista funcional | Diagrama AS-IS validado |
| Definicion de reglas de negocio y topes de monto | Analista funcional + GH | Documento de reglas v1 |
| Clasificacion de viaticos segun Art. 130 CST | Analista funcional + Legal | Reglas legales parametrizadas |
| Identificacion de integraciones (SAP OData, correo) | Arquitecto | Contrato tecnico de integracion |
| Configurar proyecto en Azure DevOps | Desarrollador | Proyecto con Boards, Repos y Pipelines base |
| Registrar Power Apps Developer Plan | Desarrollador | Ambiente de desarrollo activo |
| Crear backlog en Azure DevOps Boards | Product Owner | EPICs, HUs y Tasks creadas |
| Definir Definition of Done por HU | Equipo | DoD documentado |

---

## Fase 2: Diseno de Arquitectura (Semana 2)

### Objetivo
Definir la arquitectura tecnica, modelo de datos y seguridad.

### Tareas

| Tarea | Responsable | Entregable |
|-------|-------------|-----------|
| Crear tablas transaccionales en Dataverse | Desarrollador | Solicitudes, Aprobaciones, Pagos, Documentos, Auditoria, Detalle_Gastos |
| Crear tablas de configuracion en Dataverse | Desarrollador | CONFIG_TOPES, CONFIG_NIVELES, CONFIG_CATEGORIAS, CONFIG_ESTADOS |
| Crear tablas SAP simuladas en Dataverse | Desarrollador | SAP_INSTRUCCION_PAGO, SAP_CONFIRMACION_PAGO, SAP_MAESTRO_EMPLEADOS, SAP_CENTROS_COSTO |
| Cargar datos iniciales de configuracion | Desarrollador | Topes de monto, categorias con regla salarial, niveles de aprobacion |
| Cargar datos de prueba en SAP_MAESTRO_EMPLEADOS | Desarrollador | Empleados de prueba con PERNR y centros de costo |
| Configurar roles de seguridad en Dataverse | Desarrollador | Roles: Empleado, Jefe, GH, Finanzas, Admin |
| Crear grupos de seguridad en Azure AD | TI | Grupos Viaticos-* creados y poblados con usuarios de prueba |
| Mapear grupos AD a roles Dataverse | Desarrollador + TI | Mapeo funcional verificado |
| Configurar pipeline CI/CD base en Azure DevOps | Desarrollador | Pipeline de exportacion e importacion de solucion |
| Documentar arquitectura final | Arquitecto | DiagramaArquitectura.md actualizado |

---

## Fase 3: Desarrollo (Semanas 3-4)

### Semana 3 - Sprint 1: MVP Basico

**Historias:** HU-01, HU-03, HU-04, HU-05, HU-12, HU-13, HU-14, HU-18

| Componente | Tarea | HU |
|-----------|-------|-----|
| Power Apps | Formulario de solicitud con campos, validaciones y desglose de gastos por categoria | HU-01 |
| Power Apps | Selector de tipo de viatico (Ocasional/Permanente) con justificacion obligatoria | HU-01 |
| Power Apps | Selector de medio de pago (anticipo, tarjeta corporativa, mixto) | HU-01 |
| Power Apps | Control de carga de documentos | HU-03 |
| Power Apps | Pantalla Mis Solicitudes con estado, fecha y monto | HU-14 |
| Power Apps | Detalle de solicitud con timeline de eventos | HU-14 |
| Power Automate | Flujo de validacion de solicitud (campos, topes, desglose) | HU-01 |
| Power Automate | Flujo de aprobacion nivel 1 (Start and Wait for Approval) | HU-04, HU-05 |
| Power Automate | Flujo de notificacion por creacion de solicitud | HU-12 |
| Power Automate | Flujo de notificacion por cambio de estado | HU-13 |
| Power Automate | Flujo de auditoria automatica | HU-10 |
| Dataverse | Configurar reglas de negocio (campos obligatorios, validaciones) | HU-18 |
| Seguridad | Verificar RBAC por rol con usuarios de prueba | HU-18 |

### Semana 4 - Sprint 2: Flujo Completo (MVP E2E)

**Historias:** HU-06, HU-07, HU-08, HU-09, HU-10

| Componente | Tarea | HU |
|-----------|-------|-----|
| Power Automate | Flujo de aprobacion multinivel secuencial (Jefe, luego GH) | HU-06 |
| Power Automate | Flujo de instruccion de pago (escritura en SAP_INSTRUCCION_PAGO) | HU-07 |
| Power Automate | Validacion de topes de monto contra CONFIG_TOPES_MONTO | HU-08 |
| Power Automate | Flujo de confirmacion de pago (lectura de SAP_CONFIRMACION_PAGO) | HU-09 |
| Power Automate | Mapeo de identidad Azure AD a numero de empleado SAP | HU-07 |
| Power Apps | Vista de historial de aprobaciones por solicitud | HU-10 |
| Power Apps | Indicador visual de progreso de solicitud | HU-14 |
| Pruebas | Prueba E2E: crear, aprobar, pagar, verificar auditoria | Todas |

**Entregable: MVP funcional**

---

## Fase 4: Pruebas y Validacion (Semana 5)

### Objetivo
Asegurar calidad, precision y cumplimiento.

### Plan de pruebas

| Tipo | Alcance | Metodo |
|------|---------|--------|
| Funcional unitario | Cada HU individualmente | Casos de prueba manuales |
| Integracion | Flujo E2E: crear, aprobar (2 niveles), pagar | Ejecucion en ambiente Test |
| Seguridad / RBAC | Cada rol accede solo a lo permitido | Pruebas con usuario de prueba por rol |
| Reglas de negocio | Topes de monto, desglose obligatorio, clasificacion legal | Casos de borde |
| Regresion | Re-ejecutar casos tras correcciones | Suite documentada |
| UAT | Validacion con usuarios reales de GH y Finanzas | Sesiones guiadas con casos reales |

### Casos de prueba criticos

| ID | Caso | Resultado esperado |
|----|------|--------------------|
| TC-01 | Crear solicitud con todos los campos validos y desglose completo | Solicitud guardada en estado Enviada |
| TC-02 | Crear solicitud sin seleccionar tipo de viatico | Error de validacion |
| TC-03 | Crear solicitud sin desglose de gastos | Error de validacion |
| TC-04 | Solicitud con monto superior al tope | Bloqueada con mensaje |
| TC-05 | Jefe aprueba solicitud | Estado cambia a Aprobada_Jefe |
| TC-06 | Jefe rechaza sin comentario | Error: comentario obligatorio |
| TC-07 | GH aprueba despues de Jefe | Estado = Aprobada_GH, se genera instruccion SAP |
| TC-08 | Confirmacion de pago | Estado = Pagada, correo al solicitante |
| TC-09 | Empleado intenta aprobar | Accion denegada por RBAC |
| TC-10 | Viatico permanente con hospedaje | Alerta a GH por incidencia salarial |
| TC-11 | Auditoria completa | Todos los eventos registrados en orden |

---

## Fase 5: Despliegue y Adopcion (Semana 6)

### Objetivo
Salida a produccion controlada.

### Tareas

| Tarea | Detalle |
|-------|---------|
| Exportar solucion managed | pac solution export --managed desde Dev |
| Ejecutar pipeline Azure DevOps | Import automatico a ambiente Test, validacion, aprobacion para Prod |
| Configurar conexiones de produccion | Correo, Dataverse de produccion (si aplica) |
| Activar flujos de Power Automate | Verificar triggers y conexiones |
| Grupo piloto | 5-10 usuarios de GH para validacion inicial en produccion |
| Capacitacion | Sesiones por rol: empleados, jefes, GH, finanzas |
| Comunicacion | Comunicado organizacional sobre nueva herramienta |
| Monitoreo activo | Revisar errores de flujo y tiempos de respuesta |
| Plan de rollback | Revertir a solucion anterior si se detectan problemas criticos |

---

## Fase 6: Estabilizacion y Mejoras (Semanas 7-8)

### Semana 7: Estabilizacion

| Tarea | Detalle |
|-------|---------|
| Monitoreo de KPIs | Solicitudes procesadas, tiempos de aprobacion, errores |
| Ajustes de flujos | Correccion de errores y optimizacion de tiempos |
| HU-02: Edicion de borrador | Habilitar edicion controlada |
| HU-11: Logs de sistema | Vista de logs de ejecucion para administrador |
| HU-15: Dashboard basico | Panel con filtros y vistas por rol |

### Semana 8: Mejoras

| Tarea | Detalle |
|-------|---------|
| HU-16: OCR piloto | Integrar AI Builder para extraccion de datos de facturas |
| HU-17: Deteccion de duplicados | Reglas basicas de deteccion por NIT, factura y fecha |
| Power BI (opcional) | Dashboard ejecutivo con metricas de solicitudes y costos |
| Integracion SAP real | Si el endpoint OData esta disponible: reemplazar tablas simuladas |
| Documentacion final | Actualizar todos los documentos del proyecto |

---

## Resumen de Entregables por Fase

| Fase | Semana | Entregable |
|------|--------|-----------|
| Descubrimiento | S1 | Backlog en Azure DevOps, reglas de negocio, ambiente Dev |
| Arquitectura | S2 | Tablas Dataverse, RBAC, pipeline CI/CD, datos de prueba |
| Sprint 1 | S3 | Formulario, aprobacion N1, notificaciones, RBAC |
| Sprint 2 | S4 | MVP E2E funcional (multinivel, SAP, auditoria) |
| Pruebas | S5 | MVP validado con UAT |
| Despliegue | S6 | Sistema en produccion con grupo piloto |
| Estabilizacion | S7 | Ajustes, edicion, logs, dashboard basico |
| Mejoras | S8 | OCR, duplicados, Power BI, SAP real |
