# Casos de Prueba: Solicitudes (TC-SOL)

| ID | Descripcion | Pre-condicion | Pasos | Resultado Esperado |
|----|-------------|---------------|-------|-------------------|
| TC-SOL-01 | Creacion exitosa | Sesion iniciada | Ingresar destino, fechas, centro costo y desglose de gastos. Boton Enviar. | Registro en Dataverse con crb_estado = 'Enviada' (100000001). |
| TC-SOL-02 | Validacion de fechas | Formulario abierto | Ingresar Fecha Inicio > Fecha Fin. | Mostrar alerta: "La fecha de inicio debe ser anterior a la de fin". |
| TC-SOL-03 | Validacion de topes | Formulario abierto | Ingresar monto de Alimentacion > Tope configurado. | Mostrar alerta indicando el tope maximo permitido. Bloquear envio. |
| TC-SOL-04 | Desglose obligatorio | Formulario abierto | Intentar enviar sin agregar filas al desglose legal. | Bloquear envio y mostrar mensaje: "Debe desglosar los gastos segun Art. 130 CST". |

---

# Casos de Prueba: Aprobaciones (TC-APR)

| ID | Descripcion | Pre-condicion | Pasos | Resultado Esperado |
|----|-------------|---------------|-------|-------------------|
| TC-APR-01 | Aprobacion Nivel 1 | Solicitud en estado 'Enviada' | Jefe entra a consola, revisa y aprueba. | crb_estado cambia a 'Aprobada Jefe'. Se crea registro de aprobacion N2. |
| TC-APR-02 | Rechazo con motivo | Solicitud en estado 'Enviada' | Jefe rechaza sin poner comentario. | El sistema bloquea la accion y exige el comentario. |
| TC-APR-03 | Flujo Secuencial | Aprobacion N1 pendiente | Intentar aprobar nivel 2 (GH) antes que el 1. | La solicitud no debe aparecer en la cola de GH hasta ser aprobada por el Jefe. |

---

# Casos de Prueba: Pagos e Integracion (TC-PAG)

| ID | Descripcion | Pre-condicion | Pasos | Resultado Esperado |
|----|-------------|---------------|-------|-------------------|
| TC-PAG-01 | Envio a SAP exitoso | Solicitud Aprobada GH | Esperar ejecucion de flujo de pago. | Registro creado en crb_sap_instruccion_pago con id_transaccion unico. |
| TC-PAG-02 | Confirmacion de Pago | Estado 'En Pago' | Simular entrada en tabla crb_sap_confirmacion_pago. | Solicitud cambia a 'Pagada'. Correo enviado al empleado. |
| TC-PAG-03 | Idempotencia | Re-envio manual | Intentar enviar la misma solicitud dos veces a SAP. | El flujo debe detectar el id_transaccion previo y evitar el duplicado. |
