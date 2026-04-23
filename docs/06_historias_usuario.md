# Historias de Usuario - Proyecto Viaticos

## EPIC 1: Gestion de Solicitudes

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-01 | Como empleado, quiero registrar una solicitud de viaticos con mis datos, destino y desglose de gastos por categoria, para iniciar el proceso de aprobacion cumpliendo con el Art. 130 CST | Alta | Sprint 1 | Formulario valida campos obligatorios, exige tipo de viatico y desglose por categoria. Solicitud se persiste en Dataverse con estado Enviada |
| HU-02 | Como empleado, quiero editar una solicitud en estado Borrador, para corregir datos antes de enviarla | Media | Sprint 3 | Solo solicitudes en estado Borrador son editables. Cambios se registran en auditoria |
| HU-03 | Como empleado, quiero adjuntar documentos de soporte a mi solicitud, para respaldar la solicitud con evidencia | Alta | Sprint 1 | Permite cargar archivos (PDF, JPG, PNG). Archivo se almacena en columna de archivo de Dataverse y queda vinculado a la solicitud |

---

## EPIC 2: Aprobaciones

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-04 | Como aprobador, quiero aprobar una solicitud asignada a mi nivel, para avanzar el proceso con trazabilidad | Alta | Sprint 1 | Aprobador autorizado puede aprobar. Estado cambia segun nivel. Se registra en auditoria con fecha y usuario |
| HU-05 | Como aprobador, quiero rechazar una solicitud con un comentario obligatorio, para que el solicitante conozca el motivo | Alta | Sprint 1 | Rechazo sin comentario muestra error. Con comentario: estado cambia a Rechazada, se notifica al solicitante con motivo |
| HU-06 | Como sistema, debo ejecutar un flujo de aprobacion multinivel secuencial (Jefe, luego GH), para garantizar que no se salten niveles | Alta | Sprint 2 | No avanza a nivel 2 sin aprobacion del nivel 1. Cada nivel solo ve solicitudes pendientes de su nivel |

---

## EPIC 3: Pagos e Integracion

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-07 | Como sistema, debo enviar una instruccion de pago a SAP cuando la solicitud este completamente aprobada, para iniciar la transferencia | Alta | Sprint 2 | Solicitud aprobada se escribe en SAP_INSTRUCCION_PAGO con id_transaccion unico. Estado cambia a En_Pago |
| HU-08 | Como sistema, debo validar que los montos de la solicitud no excedan los topes configurados, para controlar el gasto | Alta | Sprint 2 | Solicitud con monto superior al tope se bloquea con mensaje de error. Topes son configurables en CONFIG_TOPES_MONTO |
| HU-09 | Como area de finanzas, quiero confirmar el pago de un viatico, para actualizar el estado y notificar al empleado | Alta | Sprint 2 | Confirmacion actualiza PAGOS.estado_pago y SOLICITUD.estado a Pagada. Se notifica al solicitante |

---

## EPIC 4: Auditoria

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-10 | Como usuario de GH, quiero consultar el historial completo de aprobaciones de una solicitud, para garantizar control y cumplimiento | Alta | Sprint 2 | Muestra todos los eventos en orden cronologico: creacion, aprobaciones, rechazos, pagos |
| HU-11 | Como administrador, quiero ver los logs de ejecucion del sistema, para diagnosticar errores en flujos e integraciones | Media | Sprint 3 | Tabla de auditoria muestra accion, usuario, fecha y detalle de cada evento |

---

## EPIC 5: Notificaciones

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-12 | Como empleado, quiero recibir un correo de confirmacion cuando creo una solicitud, para saber que fue registrada correctamente | Alta | Sprint 1 | Correo enviado con numero de solicitud, destino y monto estimado |
| HU-13 | Como empleado, quiero recibir notificaciones cuando mi solicitud cambie de estado, para hacer seguimiento sin depender de consultas manuales | Alta | Sprint 1 | Correo enviado en cada cambio de estado: aprobado, rechazado, en pago, pagado |

---

## EPIC 6: Consulta y UX

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-14 | Como empleado, quiero consultar el estado actual de mi solicitud y ver su historial, para hacer seguimiento sin depender de correos | Alta | Sprint 1 | Pantalla muestra estado actual, timeline de eventos y documentos adjuntos |
| HU-15 | Como usuario, quiero un panel con filtros para ver mis solicitudes o las de mi equipo, para gestionar multiples solicitudes | Media | Sprint 3 | Lista con filtros por estado, fecha, monto y destino. Respeta permisos RBAC |

---

## EPIC 7: Inteligencia Artificial (Post-MVP)

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-16 | Como empleado, quiero que el sistema extraiga datos de mis facturas automaticamente, para reducir el ingreso manual | Media | Sprint 3 | OCR (AI Builder) extrae nombre del proveedor, fecha, monto e impuestos |
| HU-17 | Como sistema, debo detectar posibles duplicados y anomalias en la legalizacion de gastos, para alertar sobre posibles errores o fraude | Media | Sprint 3 | Compara NIT, factura, fecha y monto contra registros previos. Genera alerta si hay coincidencia |

---

## EPIC 8: Seguridad

| ID | Historia | Prioridad | Sprint | Criterio de aceptacion |
|----|----------|----------|--------|----------------------|
| HU-18 | Como administrador, quiero que cada rol solo acceda a las acciones y datos permitidos, para cumplir con el principio de minimo privilegio | Alta | Sprint 1 | Matriz RBAC validada: Empleado, Jefe, GH, Finanzas, Admin. Cada rol probado con usuario de prueba |

---

## Organizacion por Sprint

### Sprint 1 (Semana 3) - MVP basico
HU-01, HU-03, HU-04, HU-05, HU-12, HU-13, HU-14, HU-18

### Sprint 2 (Semana 4) - Flujo completo
HU-06, HU-07, HU-08, HU-09, HU-10

### Sprint 3 (Semanas 7-8) - Mejoras
HU-02, HU-11, HU-15, HU-16, HU-17
