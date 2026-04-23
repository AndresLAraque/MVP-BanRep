# Guía de Configuración: Power Platform - Viaticos-BanRep

Esta guía detalla los pasos manuales para preparar los ambientes de Dataverse para el despliegue automatizado.

## 1. Registro de Developer Plan
1. Acceder a [Power Apps Developer Plan](https://powerapps.microsoft.com/developerplan/).
2. Registrarse con la cuenta corporativa del Banco.
3. Esto habilitará un ambiente personal de desarrollo con capacidad de Dataverse.

## 2. Creación de Ambientes (Dataverse)
Es necesario crear al menos 3 ambientes en el [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/):

| Ambiente | Tipo | Proposito |
|----------|------|-----------|
| **Dev** | Developer | Desarrollo y personalizacion |
| **Test** | Sandbox | Pruebas integrales y UAT |
| **Prod** | Production | Uso real por los usuarios |

**Importante**: Asegurarse de que la opción "Enable Dynamics 365 apps" esté en **No** para mantener la ligereza de la solución, a menos que se requiera específicamente.

## 3. Registro de App (Service Principal)
Para permitir que Azure DevOps se comunique con Power Platform de forma segura:

1. Ir al portal de **Azure / Entra ID**.
2. **App Registrations** > **New Registration**.
   - Nombre: `SP-DevOps-PowerPlatform`.
3. Crear un **Client Secret** y guardarlo de forma segura.
4. En **API Permissions**, agregar `PowerApps Runtime Service` e `User.Read`.
5. En el Power Platform Admin Center:
   - Ir a la configuración del ambiente (Dev/Test/Prod).
   - **Users + permissions** > **Application users**.
   - Agregar el App ID registrado arriba.
   - Asignar el rol: **System Administrator**.

## 4. Power Platform CLI (pac)
Para trabajar localmente con la solución:
1. Instale [Power Platform Tools](https://aka.ms/PowerPlatformCLI) para VS Code.
2. Comandos útiles:
   - `pac auth create`: Conectar al ambiente.
   - `pac solution clone`: Clonar solución existente.
   - `pac solution pack`: Empaquetar archivos locales.
   - `pac solution unpack`: Desempaquetar archivo .zip.
