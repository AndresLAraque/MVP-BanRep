# Mapa de Navegación - Power Apps Viaticos

El siguiente diagrama detalla el flujo de pantallas y las condiciones de transición entre ellas.

```mermaid
graph TD
    Login((Inicio Sesion)) -->|Entra ID SSO| Auth{¿Rol?}
    
    Auth -->|Admin| Config[scr_AdminConfig]
    Auth -->|Otros| Dashboard[scr_EmployeeDashboard]
    
    Dashboard -->|Boton +| Form[scr_RequestForm]
    Dashboard -->|Seleccionar Solicitud| Tracking[scr_RequestTracking]
    
    Form -->|Guardar Borrador| Dashboard
    Form -->|Enviar| Success[scr_SubmitSuccess]
    Success --> Dashboard
    
    Auth -->|Jefe / GH| Console[scr_ApprovalConsole]
    Console -->|Ver Detalle| Tracking
    
    Tracking -->|Aprobador: Ejecutar Accion| Console
```

## Resumen de Transiciones

1.  **Contexto de Solicitud**: Al pasar de la consola de aprobación al tracking, se pasa el ID de la solicitud como parámetro global.
2.  **Seguridad de Navegacion**: Las pantallas de administración y aprobación tienen reglas `OnVisible` que redirigen al Dashboard si el usuario no cuenta con el rol de seguridad adecuado en Dataverse.
3.  **Manejo de Errores**: Si ocurre un error de conexión, se muestra una barra de notificación superior (Azul con texto Oro) indicando al usuario que reintente.
