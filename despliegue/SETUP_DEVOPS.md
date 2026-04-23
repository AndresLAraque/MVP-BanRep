# Guía de Configuración: Azure DevOps - Proyecto Viaticos-BanRep

Esta guía detalla los pasos manuales necesarios para configurar el entorno de Azure DevOps para el proyecto de gestión de viáticos.

## 1. Creación del Proyecto
1. Acceder a `dev.azure.com/{TuOrganizacion}`.
2. Click en **New Project**.
3. Nombre: `Viaticos-BanRep`.
4. Visibilidad: **Private**.
5. Control de Versiones: **Git**.
6. Work Item Process: **Agile**.

## 2. Configuración de Boards (Agile)

### EPICs Sugeridas
1. **Infraestructura y DevOps**: Pipelines, ambientes y seguridad.
2. **Modelo de Datos**: Tablas y reglas en Dataverse.
3. **App Solicitante**: Portal de Power Apps para empleados.
4. **App Aprobador**: Dashboard de aprobaciones y consultas.
5. **Automatizacion de Procesos**: Flujos de Power Automate.
6. **Integracion SAP**: Conectores y lógica de pago.
7. **Seguridad y Auditoria**: Roles RBAC y logs inmutables.
8. **Pruebas y QA**: Casos de prueba y UAT.

### Backlog Inicial
- Cargar las Historias de Usuario (HUs) definidas en `docs/06_historias_usuario.md`.

## 3. Repositorio Git
1. El repositorio debe seguir la estructura actual del espacio de trabajo:
    - `/solucion`: Código fuente y esquemas de Dataverse.
    - `/docs`: Documentación técnica y de negocio.
    - `/pruebas`: Plan de pruebas y casos.
    - `/despliegue`: Pipelines y guías de operación.

## 4. Extensiones Necesarias
Para que los pipelines funcionen, instale la siguiente extensión desde el Marketplace:
- **Power Platform Build Tools** (de Microsoft).

## 5. Service Connections
1. Ir a **Project Settings** > **Service connections**.
2. Crear una nueva conexión de tipo **Power Platform**.
3. Configure una conexión por cada ambiente:
    - `PowerPlatform-Dev`
    - `PowerPlatform-Test`
    - `PowerPlatform-Prod`
4. Se recomienda usar la opción **Service Principal / Client Secret** (ver `SETUP_POWERPLATFORM.md`).
