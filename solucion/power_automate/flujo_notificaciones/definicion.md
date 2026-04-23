# Definicion de Flujo: Motor de Notificaciones

Flujo centralizado para el envío de alertas por Correo y Microsoft Teams.

## 1. Trigger (Disparador)
- **Evento**: Manual o HTTP Request desde otros flujos.
- **Entrada**: Identificador de solicitud, Tipo de Notificación, Email Destinatario.

## 2. Lógica de Envío

### A. Canal de Correo (Outlook)
- Seleccionar la plantilla HTML desde `plantillas_correo.md`.
- Reemplazar variables: `{{Nombre}}`, `{{Destino}}`, `{{Monto}}`, `{{Estado}}`.
- Enviar con importancia "Alta" para aprobaciones.

### B. Canal de Teams (Adaptive Cards)
- Generar el JSON de la tarjeta adaptable según el estado.
- Publicar en el chat del usuario o canal de equipo usando el conector de **Workflows for Teams**.

---

# Definicion de Flujo: Auditoria Inmutable

Garantiza que cada evento quede registrado para cumplimiento normativo.

## 1. Trigger (Disparador)
- **Evento**: Cambio en cualquier tabla del sistema (Solicitudes, Detalle de Gastos, Aprobaciones, Pagos).

## 2. Acción
- Crear una fila en `crb_auditoria` con:
    - ID Solicitud.
    - Usuario (desde el contexto de la ejecución).
    - Acción (ej: "Actualizacion de monto", "Aprobacion Nivel 1").
    - Detalle (JSON con el valor anterior y el nuevo valor).
