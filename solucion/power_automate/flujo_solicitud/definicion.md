# Definición de Flujo: Registro y Validación de Solicitud

Este flujo se encarga del procesamiento inicial de cada solicitud enviada por un empleado.

## 1. Trigger (Disparador)
- **Proveedor**: Microsoft Dataverse.
- **Evento**: Cuando se crea o modifica una fila en la tabla `crb_solicitudes`.
- **Condición**: `crb_estado` es igual a `100000001` (Enviada).

## 2. Acciones de Lógica

### A. Validación de Integridad
- **Verificación**: ¿Existen registros vinculados en `crb_detalle_gastos`?
- **Validación de Topes**: 
    - Por cada registro de gasto, buscar el tope en `crb_config_topes_monto` segun `crb_destino_tipo` y `crb_categoria_gasto`.
    - Si el monto excede el tope, el flujo se detiene y actualiza la solicitud a estado `Rechazada` por "Exceso de Tope".

### B. Cálculo de Totales
- Sumar todos los montos del desglose.
- Validar que la suma coincida con `crb_monto_estimado` de la solicitud.

### C. Inicio de Aprobación
- Obtener el aprobador (Jefe Inmediato) desde la tabla `crb_sap_centros_costo` usando el centro de costo de la solicitud.
- Crear una nueva fila en `crb_aprobaciones` con `nivel` = 1.

## 3. Notificaciones Iniciales
- **Email (Solicitante)**: Confirmación de enviado (Plantilla Azul/Oro).
- **Notificación en Teams (Jefe)**: Ver sección de Adaptive Cards en `plantillas_correo.md`.
