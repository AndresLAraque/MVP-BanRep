# MVP Sistema de Gestion de Viaticos

## Banco de la Republica - Direccion de Gestion Humana

---

## Descripcion

Sistema digital para la gestion integral del proceso de viaticos destinados a equipos que viajan a organizaciones nacionales e internacionales para conocer implementaciones de inteligencia artificial. Reemplaza el proceso manual (correo electronico y plantillas Excel) por una solucion automatizada con trazabilidad completa, aprobaciones controladas y cumplimiento del Art. 130 del Codigo Sustantivo del Trabajo.

## Problema

1. Las solicitudes de viaticos se realizan por correo y Excel sin trazabilidad de estados ni responsables
2. Las aprobaciones involucran multiples areas sin registro de auditoria ni SLAs
3. La documentacion se llena manualmente con errores frecuentes y versiones no controladas
4. La legalizacion de gastos se hace en formatos dispersos con inconsistencias
5. La notificacion de pago es manual y la conciliacion se realiza sin controles automatizados

## Tecnologias

| Componente | Tecnologia |
|-----------|-----------|
| Frontend | Power Apps (Model-Driven App) |
| Orquestacion | Power Automate (Flujos cloud) |
| Datos | Dataverse |
| Integracion SAP | Tablas simuladas formato OData / S/4HANA |
| Identidad | Azure AD / Entra ID (SSO + RBAC) |
| DevOps | Azure DevOps (Boards, Repos, Pipelines) |
| Correo | Conector Office 365 Outlook |

## Estructura del Proyecto

```
MVP/
|-- README.md                               Este archivo
|
|-- docs/                                   Documentacion del proyecto
|   |-- 01_plan_implementacion.md           Plan general y decisiones
|   |-- 02_propuesta_proceso.md             Flujos AS-IS y TO-BE
|   |-- 03_arquitectura.md                  Diagramas C4, RBAC, DevOps, flujos
|   |-- 04_modelo_datos.md                  Entidades, campos, SAP simulado, topes
|   |-- 05_marco_legal.md                   Art. 130 CST, jurisprudencia, reglas
|   |-- 06_historias_usuario.md             18 HU con criterios de aceptacion
|   |-- 07_backlog.md                       Backlog detallado por modulo
|   |-- 08_cronograma.md                    Cronograma 8 semanas con pruebas
|
|-- solucion/                               Artefactos de la solucion
|   |-- dataverse/
|   |   |-- tablas/                         Definiciones de tablas exportadas
|   |   |-- reglas/                         Reglas de negocio
|   |   |-- roles/                          Roles de seguridad
|   |   |-- configuracion/                  Datos de configuracion
|   |   |-- sap_simulado/                   Tablas que replican esquema SAP HANA
|   |-- power_apps/                         Solucion de la aplicacion
|   |-- power_automate/
|       |-- flujo_solicitud/                Validacion y registro
|       |-- flujo_aprobacion/               Multinivel secuencial
|       |-- flujo_pago/                     Instruccion SAP
|       |-- flujo_notificaciones/           Correos automaticos
|       |-- flujo_auditoria/               Registro de eventos
|
|-- pruebas/                                Calidad y validacion
|   |-- casos/                             Casos de prueba documentados
|   |-- evidencias/                        Capturas y resultados
|   |-- uat/                               Checklist y resultados UAT
|
|-- despliegue/                             Despliegue y operacion
    |-- pipelines/                         Definiciones de Azure DevOps Pipelines
```

## Requisitos para Desarrollo

1. Cuenta de trabajo o escuela respaldada por Microsoft Entra ID
2. Power Apps Developer Plan (gratuito): https://powerapps.microsoft.com/developerplan/
3. Azure DevOps Free Tier (hasta 5 usuarios): https://dev.azure.com/
4. Navegador web moderno (Edge, Chrome)

## Documentacion

El punto de entrada principal es [01_plan_implementacion.md](docs/01_plan_implementacion.md), que contiene las decisiones confirmadas y referencias a todos los documentos detallados.
