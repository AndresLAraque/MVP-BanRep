# Definición de Flujo: Aprobación Multinivel y Secuencial

Este flujo orquestra las decisiones de los aprobadores (Jefe Inmediato y Gestion Humana).

## 1. Trigger (Disparador)
- **Proveedor**: Microsoft Dataverse.
- **Evento**: Cuando se actualiza una fila en la tabla `crb_aprobaciones`.
- **Condición**: `crb_estado` cambia a `Aprobada` o `Rechazada`.

## 2. Orquestación según Nivel

### Caso: Jefe Aprueba (Nivel 1)
1.  Actualizar `crb_solicitudes` a estado "Aprobada por Jefe".
2.  Registrar evento en `crb_auditoria`.
3.  Consultar la siguiente aprobacion requerida en `crb_config_niveles_aprobacion`.
4.  Crear registro de aprobacion para **Gestion Humana** (Nivel 2).
5.  Enviar **Adaptive Card** a Teams del equipo de GH.

### Caso: GH Aprueba (Nivel 2)
1.  Actualizar `crb_solicitudes` a estado "Aprobada por GH".
2.  Registrar evento en `crb_auditoria`.
3.  Disparar automáticamente el **Flujo de Pago (SAP)**.

### Caso: Rechazo (Cualquier nivel)
1.  **Validación**: ¿El campo `crb_comentario` está lleno? (Validado en UI pero re-validado aquí).
2.  Actualizar solicitud a estado "Rechazada".
3.  Enviar correo al solicitante con el motivo (Plantilla con bordes Oro).

## 3. Manejo de Tiempos (SLA)
- Si una aprobación está pendiente por más de 48 horas:
    - Enviar correo de recordatorio al aprobador.
    - Escalar notificación a la tabla de auditoría como "Aviso de retraso".
