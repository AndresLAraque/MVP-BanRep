# Procedimiento de Rollback - Viaticos-BanRep

Este documento describe las acciones a seguir en caso de que un despliegue falle o cause una regresión crítica en los ambientes de Test o Producción.

## Escenario A: Falla durante la Importación del Pipeline
Si el pipeline de Azure DevOps marca error en la tarea de Import-Solution:
1. **Revisar Logs**: Identificar si es un problema de dependencias faltantes o tiempo de espera (Timeout).
2. **Corregir en Dev**: Realizar la corrección técnica en el ambiente de Desarrollo.
3. **Re-exportar**: Ejecutar nuevamente el pipeline de exportación y reintentar el despliegue.

## Escenario B: Regresión funcional detectada post-despliegue
Si la solución se importó correctamente pero la aplicación no funciona como se esperaba:

### 1. Reversión de la Solución Managed
Como se utilizan **Managed Solutions**, la forma más segura de revertir es:
1. Localizar la versión anterior exitosa de la solución (el archivo `.zip` en los artefactos de Azure DevOps o en el historial de Git).
2. Incrementar el número de versión de la solución en un entorno de "despliegue técnico" o manual.
3. Importar la versión anterior sobre la actual. Dataverse tratará esto como una actualización (siempre que la versión sea mayor).

### 2. Eliminación de Capas (Unmanaged Layers)
Si los cambios no se reflejan debido a personalizaciones directas en el ambiente de destino:
1. Ir a la solución en el ambiente afectado.
2. Seleccionar el componente problemático.
3. Elegir **See solution layers**.
4. Eliminar la **Unmanaged Layer** que esté sobre la capa de la solución administrada.

### 3. Comunicación a Usuarios
1. Notificar al canal de soporte (`Viaticos-Soporte` en Teams) sobre la indisponibilidad temporal.
2. Informar el tiempo estimado de restauración.

## Contactos de Emergencia
- Administrador Dataverse: [Nombre/Email]
- Desarrollador Lead: [Nombre/Email]
- Soporte Microsoft: Ticket Premium vía Microsoft 365 Admin Center.
