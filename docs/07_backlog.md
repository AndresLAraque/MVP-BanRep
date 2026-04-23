# Backlog Funcional - Proyecto Viaticos

## Modulo 1: Solicitudes

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| Formulario de solicitud | Formulario con campos: destino, pais, motivo, fechas, monto, moneda, centro de costo, tipo de viatico | Alta | HU-01 |
| Clasificacion legal | Selector obligatorio de tipo de viatico (Ocasional/Permanente) con justificacion | Alta | HU-01 |
| Desglose de gastos | Tabla de desglose por categoria (Hospedaje, Alimentacion, Transporte, Representacion) con calculo de incidencia salarial | Alta | HU-01 |
| Validaciones de formulario | Campos obligatorios, monto mayor a cero, fecha inicio menor a fecha fin, desglose completo | Alta | HU-01 |
| Carga de documentos | Control de adjuntos (PDF, JPG, PNG) almacenados en columna de archivo de Dataverse | Alta | HU-03 |
| Guardar como borrador | Guardar solicitud en estado Borrador sin disparar flujos | Alta | HU-01 |
| Enviar solicitud | Cambiar estado a Enviada y disparar flujo de validacion y aprobacion | Alta | HU-01 |
| Medio de pago | Selector de medio de pago: anticipo en efectivo, tarjeta corporativa, mixto | Alta | HU-01 |
| Edicion de borrador | Permitir editar solicitudes en estado Borrador. Bloquear edicion en otros estados | Media | HU-02 |

---

## Modulo 2: Aprobaciones

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| Aprobacion nivel 1 (Jefe) | Flujo de Power Automate con accion Start and Wait for Approval | Alta | HU-04 |
| Rechazo con comentario | Validar que el comentario no este vacio al rechazar | Alta | HU-05 |
| Aprobacion nivel 2 (GH) | Segundo nivel secuencial, disparado automaticamente al completar nivel 1 | Alta | HU-06 |
| Niveles configurables | Tabla CONFIG_NIVELES_APROBACION para agregar o modificar niveles sin cambiar codigo | Alta | HU-06 |
| Vista de aprobador | Lista de solicitudes pendientes de aprobacion filtrada por rol y nivel | Alta | HU-04 |

---

## Modulo 3: Pagos e Integracion SAP

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| Validacion de topes | Comparar monto total y por categoria contra CONFIG_TOPES_MONTO | Alta | HU-08 |
| Generacion de instruccion de pago | Escribir en SAP_INSTRUCCION_PAGO con id_transaccion unico (idempotencia) | Alta | HU-07 |
| Mapeo de empleado SAP | Buscar numero_empleado_sap por email corporativo en SAP_MAESTRO_EMPLEADOS | Alta | HU-07 |
| Confirmacion de pago | Actualizar PAGOS y SOLICITUD al recibir confirmacion en SAP_CONFIRMACION_PAGO | Alta | HU-09 |
| Conciliacion de tarjetas | Cruce de movimientos de tarjeta corporativa contra gastos registrados | Media | Post-MVP |
| Conciliacion de anticipos | Cruce de anticipo entregado contra gastos legalizados | Media | Post-MVP |

---

## Modulo 4: Auditoria y Trazabilidad

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| Registro automatico de eventos | Cada cambio de estado genera registro en AUDITORIA via flujo dedicado | Alta | HU-10 |
| Timeline de solicitud | Vista cronologica de todos los eventos de una solicitud | Alta | HU-10 |
| Logs de sistema | Registro de ejecuciones de flujos, errores y excepciones | Media | HU-11 |

---

## Modulo 5: Notificaciones

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| Correo de creacion | Notificar al solicitante y al jefe cuando se crea una solicitud | Alta | HU-12 |
| Correo de cambio de estado | Notificar al solicitante en cada transicion de estado | Alta | HU-13 |
| Correo al aprobador | Notificar al siguiente aprobador cuando le llega una solicitud pendiente | Alta | HU-13 |
| Correo a Finanzas | Notificar cuando una solicitud esta lista para pago | Alta | HU-13 |
| Plantillas configurables | Tabla CONFIG_PLANTILLAS_CORREO con plantillas editables por el administrador | Media | HU-13 |

---

## Modulo 6: Consulta y UX

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| Pantalla Mis Solicitudes | Lista de solicitudes del empleado con estado, fecha y monto | Alta | HU-14 |
| Detalle de solicitud | Vista completa con datos, desglose, documentos y timeline | Alta | HU-14 |
| Indicador de estado visual | Barra de progreso: Enviada, Jefe, GH, Pago, Pagada | Alta | HU-14 |
| Filtros y busqueda | Filtrar por estado, fecha, monto y destino | Media | HU-15 |
| Vista de equipo (Jefe) | Lista de solicitudes del equipo a cargo | Media | HU-15 |

---

## Modulo 7: Inteligencia Artificial (Post-MVP)

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| OCR de facturas | Extraccion de datos con AI Builder: proveedor, fecha, monto, impuestos | Media | HU-16 |
| Deteccion de duplicados | Comparar NIT, numero de factura, fecha y monto contra registros previos | Media | HU-17 |
| Alertas de anomalia | Reglas para identificar gastos atipicos por concepto, monto o frecuencia | Media | HU-17 |

---

## Modulo 8: Seguridad y Configuracion

| Item | Descripcion | Prioridad | HU relacionada |
|------|------------|----------|---------------|
| Roles de seguridad en Dataverse | Empleado, Jefe, GH, Finanzas, Admin con permisos CRUD por tabla | Alta | HU-18 |
| Grupos de seguridad en Azure AD | Crear grupos: Viaticos-Empleados, Viaticos-Jefes, Viaticos-GH, Viaticos-Finanzas, Viaticos-Admin | Alta | HU-18 |
| Mapeo roles-grupos | Vincular grupos de Azure AD con roles de seguridad de Dataverse | Alta | HU-18 |
| Tablas de configuracion | CONFIG_TOPES, CONFIG_NIVELES, CONFIG_CATEGORIAS, CONFIG_ESTADOS, CONFIG_PLANTILLAS | Alta | Transversal |
