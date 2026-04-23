# Arquitectura del Sistema - Viaticos

## 1. Vista General

```mermaid
graph TB
    subgraph "Usuarios"
        U["Empleado - Jefe - GH - Finanzas - Admin"]
    end

    subgraph "Presentacion"
        PA["Power Apps\nModel-Driven App"]
    end

    subgraph "Orquestacion"
        PF["Power Automate\nFlujos de proceso"]
    end

    subgraph "Datos"
        DV["Dataverse\nTablas transaccionales\ny configuracion"]
        SAP_SIM["Tablas SAP simuladas\nFormato OData S/4HANA"]
    end

    subgraph "Seguridad"
        AAD["Azure AD / Entra ID\nSSO y RBAC"]
    end

    subgraph "DevOps"
        ADO["Azure DevOps\nBoards - Repos - Pipelines"]
    end

    U --> PA
    PA --> DV
    DV --> PF
    PF --> DV
    PF --> SAP_SIM
    AAD --> PA
    ADO --> DV
```

---

## 2. Contexto del Sistema (C1)

Vista de alto nivel que muestra el sistema y sus interacciones externas.

```mermaid
flowchart LR
    Usuario["Empleado\nAprobador\nFinanzas"] -->|"Registra y aprueba\nsolicitudes"| Sistema["Sistema de Gestion\nde Viaticos"]
    Sistema -->|"Envia instrucciones\nde pago"| SAP["SAP S/4HANA"]
    SAP -->|"Confirma pagos"| Sistema
    Sistema -->|"Notificaciones\nautomaticas"| Email["Servicio de Correo"]
    AAD["Azure AD"] -->|"Autenticacion\ny roles"| Sistema
```

---

## 3. Contenedores (C2)

```mermaid
flowchart TB
    subgraph "Frontend"
        UI["Power Apps\nFormulario y consulta"]
    end

    subgraph "Procesos"
        WF["Power Automate\nFlujos de aprobacion,\npago y notificacion"]
    end

    subgraph "Datos"
        DB["Dataverse\nTablas relacionales"]
        DOC["Dataverse\nColumnas de archivo"]
    end

    subgraph "Externos"
        SAP["SAP S/4HANA\nSimulado en Dataverse"]
        MAIL["Correo\nConector Outlook"]
        AUTH["Azure AD\nIdentidad"]
    end

    UI --> DB
    UI --> DOC
    UI --> WF
    WF --> DB
    WF --> SAP
    WF --> MAIL
    AUTH --> UI
    AUTH --> WF
```

---

## 4. Componentes Internos (C3)

```mermaid
flowchart TB
    subgraph "Power Apps"
        Form["Formulario de solicitud\ncon desglose legal"]
        Consult["Consulta de estado\ny timeline"]
    end

    subgraph "Power Automate"
        FlowSol["Flujo: Solicitud\nValidacion y registro"]
        FlowApr["Flujo: Aprobacion\nMultinivel secuencial"]
        FlowPay["Flujo: Pago\nInstruccion SAP"]
        FlowNot["Flujo: Notificaciones\nCorreo automatico"]
        FlowAud["Flujo: Auditoria\nRegistro de eventos"]
    end

    subgraph "Dataverse"
        T1["Solicitudes"]
        T2["Detalle de gastos"]
        T3["Aprobaciones"]
        T4["Pagos"]
        T5["Auditoria"]
        T6["Configuracion"]
    end

    Form --> FlowSol
    FlowSol --> T1
    FlowSol --> T2
    FlowApr --> T3
    FlowApr --> T5
    FlowPay --> T4
    FlowNot --> Consult
    FlowAud --> T5
    Consult --> T1
    Consult --> T3
    Consult --> T5
```

---

## 5. Flujo de Secuencia (C4)

```mermaid
sequenceDiagram
    participant Emp as Empleado
    participant App as Power Apps
    participant Flow as Power Automate
    participant DB as Dataverse
    participant SAP as SAP Simulado
    participant Mail as Correo

    Emp->>App: Crear solicitud con desglose
    App->>DB: Guardar solicitud y detalle de gastos
    App->>Flow: Disparar flujo de validacion
    Flow->>DB: Validar topes y reglas
    Flow->>DB: Crear aprobacion nivel 1
    Flow->>Mail: Notificar al jefe
    
    Note over Flow: Jefe aprueba
    
    Flow->>DB: Registrar aprobacion
    Flow->>DB: Crear aprobacion nivel 2
    Flow->>Mail: Notificar a GH
    
    Note over Flow: GH aprueba
    
    Flow->>DB: Registrar aprobacion
    Flow->>SAP: Crear instruccion de pago
    Flow->>Mail: Notificar a Finanzas
    
    Note over Flow: Finanzas confirma
    
    Flow->>DB: Actualizar estado a Pagada
    Flow->>DB: Registrar en auditoria
    Flow->>Mail: Notificar al empleado
```

---

## 6. Principios Arquitectonicos

| Principio | Aplicacion |
|-----------|-----------|
| Bajo acoplamiento | Cada flujo de Power Automate es independiente, activado por cambio de estado en Dataverse |
| Idempotencia | Toda operacion SAP incluye ID de transaccion unico para evitar duplicados |
| Auditoria desde el dia 1 | Cada cambio de estado genera registro automatico en tabla Auditoria |
| Diseno para migracion | Tablas SAP simuladas usan el mismo esquema OData que S/4HANA para migracion sin friccion |
| Configuracion sobre codigo | Reglas de monto, niveles de aprobacion, categorias y plantillas son tablas de configuracion, no codigo fijo |
| Separacion de ambientes | Dev/Test/Prod gestionados con soluciones managed via Azure DevOps Pipelines |

---

## 7. Matriz RBAC (Control de Acceso por Rol)

| Accion | Empleado | Jefe | GH | Finanzas | Admin |
|--------|----------|------|----|----------|-------|
| Crear solicitud | Solo propias | No | No | No | Todas |
| Leer solicitudes | Solo propias | Su equipo | Todas | Aprobadas | Todas |
| Editar solicitud | Solo en Borrador | No | No | No | Todas |
| Aprobar | No | Nivel 1 | Nivel 2 | No | Todas |
| Gestionar pagos | No | No | No | Si | Todas |
| Ver auditoria | Solo propias | Su equipo | Todas | Todas | Todas |
| Adjuntar documentos | Solo propias | No | No | No | Todas |
| Configuracion | No | No | No | No | Si |

### Grupos de seguridad en Azure AD

| Grupo | Rol Dataverse | Usuarios |
|-------|--------------|----------|
| Viaticos-Empleados | Empleado | Todos los empleados que solicitan viaticos |
| Viaticos-Jefes | Jefe | Jefes inmediatos con personal a cargo |
| Viaticos-GH | GH | Personal de Gestion Humana autorizado |
| Viaticos-Finanzas | Finanzas | Personal de pagos y tesoreria |
| Viaticos-Admin | Admin | Administradores funcionales del sistema |

---

## 8. Azure DevOps -- Estructura y Pipeline

### Estructura del proyecto

```
Proyecto: Viaticos-BanRep
|
|-- Boards/
|   |-- Epics (8 EPICs)
|   |-- User Stories (18 HUs)
|   |-- Tasks (desglose tecnico)
|   |-- Sprints (S1, S2, S3 + Estabilizacion)
|
|-- Repos/
|   |-- /solucion/           Soluciones Dataverse exportadas (.zip managed)
|   |-- /docs/               Documentacion del proyecto
|   |-- /pruebas/            Casos de prueba y evidencias
|   |-- /despliegue/         Configuracion de pipelines
|
|-- Pipelines/
    |-- export-solution      pac solution export --managed
    |-- import-to-test       pac solution import a Test
    |-- run-tests            Validaciones post-import
    |-- import-to-prod       Import a Prod con aprobacion manual
```

### Pipeline CI/CD

```mermaid
flowchart LR
    DEV["Ambiente Dev\nPower Apps Developer Plan"] -->|"pac solution export\n--managed"| REPO["Azure DevOps Repos\nVersionado Git"]
    REPO -->|"Pipeline automatico"| TEST["Ambiente Test\nIntegracion y UAT"]
    TEST -->|"Aprobacion manual\nen Gate"| PROD["Ambiente Prod\nDespliegue controlado"]
```

---

## 9. Flujos de Power Automate (Detalle)

### Flujo 1: Creacion y validacion de solicitud

| Aspecto | Detalle |
|---------|--------|
| Trigger | Registro nuevo en SOLICITUDES con estado = Enviada |
| Validaciones | Campos obligatorios, desglose de gastos completo, tipo de viatico seleccionado, monto vs topes, fechas coherentes |
| Acciones | Registrar auditoria, enviar correo de confirmacion, crear aprobacion nivel 1 con aprobador = jefe inmediato |

### Flujo 2: Aprobacion multinivel secuencial

| Aspecto | Detalle |
|---------|--------|
| Trigger | Cambio de estado en Aprobaciones |
| Si aprobado | Verificar si hay nivel N+1 en CONFIG_NIVELES_APROBACION. Si existe, crear siguiente aprobacion y notificar. Si no, marcar como Aprobada_GH y disparar Flujo 3 |
| Si rechazado | Validar comentario obligatorio. Marcar solicitud como Rechazada. Registrar auditoria. Notificar al solicitante |

### Flujo 3: Instruccion de pago (integracion SAP)

| Aspecto | Detalle |
|---------|--------|
| Trigger | Solicitud.estado = Aprobada_GH |
| Acciones | Generar id_transaccion unico. Buscar numero de empleado SAP por email. Construir payload OData. Escribir en SAP_INSTRUCCION_PAGO. Actualizar estado a En_Pago. Crear registro en PAGOS. Notificar a Finanzas |

### Flujo 4: Confirmacion de pago

| Aspecto | Detalle |
|---------|--------|
| Trigger | Actualizacion en SAP_CONFIRMACION_PAGO o actualizacion manual por Finanzas |
| Acciones | Buscar solicitud por id_transaccion. Actualizar PAGOS y SOLICITUD.estado = Pagada. Registrar auditoria. Notificar al empleado |

### Flujo 5: Auditoria automatica

| Aspecto | Detalle |
|---------|--------|
| Trigger | Cualquier cambio de estado en SOLICITUDES, APROBACIONES o PAGOS |
| Acciones | Registrar solicitud_id, usuario, accion, timestamp y detalle del cambio |

---

## 10. Evolucion Futura

| Componente | Proposito | Fase |
|-----------|----------|------|
| SAP S/4HANA real | Reemplazo de tablas simuladas por endpoints OData reales | Post-MVP |
| Power BI | Dashboard ejecutivo con metricas de solicitudes, tiempos y costos | Semana 8 |
| AI Builder (OCR) | Extraccion automatica de datos de facturas y recibos | Semana 8 |
| Azure Functions | Logica de negocio compleja que exceda capacidades de Power Automate | Post-MVP |
| Azure Monitor | Observabilidad centralizada de flujos, errores e integraciones | Post-MVP |
| SharePoint | Gestion documental avanzada cuando se cuente con licencia M365 | Post-MVP |
