# Definicion de Flujo: Integracion de Pago (SAP)

Este flujo simula la integración con SAP S/4HANA para la generación de la instrucción de pago.

## 1. Trigger (Disparador)
- **Evento**: Manual o automático cuando `solicitud.crb_estado` = "Aprobada por GH".

## 2. Acciones de Integracion

### A. Preparación del Envío
1.  **Idempotencia**: Generar un GUID único para el campo `crb_id_transaccion`.
2.  **Mapeo Maestro**: Buscar en `crb_sap_maestro_empleados` el número de personal (PERNR) usando el email del solicitante.
3.  **Búsqueda Salarial**: Calcular la incidencia salarial según la lógica del Art. 130 CST documentada en `solucion/dataverse/reglas/calculo_incidencia_salarial.md`.

### B. Escritura en SAP (Simulado)
1.  Crear una fila en `crb_sap_instruccion_pago` con los datos mapeados:
    - Sociedad, Centro Costo, PERNR, Monto, Moneda, Concepto, ID Transacción.
2.  Actualizar la solicitud a estado "En Pago".
3.  Crear registro en la tabla `crb_pagos` con estado "Enviado_SAP".

### C. Manejo de Respuesta
- El flujo queda a la espera de una actualización en `crb_sap_confirmacion_pago`.
- Al recibirla:
    - Actualizar estado a "Pagada" si éxito.
    - Actualizar a "Error de Pago" si falla (Notificar a Finanzas para reintento manual).

## 3. Notificaciones Post-Pago
- Enviar correo de éxito al empleado (Plantilla Azul/Oro).
