# Plantillas de Notificación - Estilo BanRep (Azul y Oro)

Este documento contiene el código fuente para los correos HTML y los JSON para las Adaptive Cards de Teams.

## 1. Plantilla de Correo (HTML)

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .container { font-family: 'Segoe UI', sans-serif; border: 1px solid #D4AF37; max-width: 600px; margin: auto; }
        .header { background-color: #002D72; color: white; padding: 20px; text-align: center; border-bottom: 5px solid #D4AF37; }
        .content { padding: 20px; color: #333; line-height: 1.6; }
        .footer { background-color: #F4F4F4; padding: 10px; font-size: 11px; text-align: center; color: #666; }
        .button { background-color: #002D72; color: #D4AF37; padding: 10px 20px; text-decoration: none; border-radius: 4px; display: inline-block; font-weight: bold; border: 1px solid #D4AF37; }
        .status-pill { background-color: #D4AF37; color: #002D72; padding: 3px 10px; border-radius: 12px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Sistema de Viáticos</h1>
        </div>
        <div class="content">
            <p>Hola <strong>{{Nombre}}</strong>,</p>
            <p>Se ha registrado una actualización en su solicitud de viáticos.</p>
            <p><strong>Estado Actual:</strong> <span class="status-pill">{{Estado}}</span></p>
            <p><strong>Detalles:</strong></p>
            <ul>
                <li><strong>Destino:</strong> {{Destino}}</li>
                <li><strong>Monto Estimado:</strong> {{Monto}}</li>
            </ul>
            <p>Para ver más detalles, haga clic en el siguiente enlace:</p>
            <p style="text-align: center;">
                <a href="{{LinkApp}}" class="button">Ver Solicitud en Power Apps</a>
            </p>
        </div>
        <div class="footer">
            Este es un mensaje automático generado por el Sistema de Viáticos del Banco de la República.
        </div>
    </div>
</body>
</html>
```

---

## 2. Adaptive Card para Teams (JSON)

```json
{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "Aprobación de Viático Pendiente",
            "color": "Accent"
        },
        {
            "type": "FactSet",
            "facts": [
                {
                    "title": "Solicitante:",
                    "value": "{{Nombre}}"
                },
                {
                    "title": "Destino:",
                    "value": "{{Destino}}"
                },
                {
                    "title": "Monto:",
                    "value": "{{Monto}}"
                }
            ]
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "Aprobar",
                    "data": {
                        "action": "approve",
                        "requestId": "{{ID}}"
                    },
                    "style": "positive"
                },
                {
                    "type": "Action.Submit",
                    "title": "Rechazar",
                    "data": {
                        "action": "reject",
                        "requestId": "{{ID}}"
                    },
                    "style": "destructive"
                },
                {
                    "type": "Action.OpenUrl",
                    "title": "Ver Detalles",
                    "url": "{{LinkApp}}"
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
}
```
