# Propuesta de Solucion - Sistema de Gestion de Viaticos

## 1. Flujo AS-IS (Estado Actual)

El proceso actual de viaticos opera de forma manual y fragmentada entre multiples areas:

```mermaid
flowchart TD
    A["Empleado redacta solicitud\nen formato Excel"] --> B["Envia correo electronico\nal jefe inmediato"]
    B --> C["Jefe revisa correo\ny responde aprobando o rechazando"]
    C --> D["Se reenvian correos\na Gestion Humana"]
    D --> E["GH valida politicas\nsin registro formal"]
    E --> F["Se notifica por correo\na Presupuesto y Compras"]
    F --> G["Finanzas recibe correo\ny procesa manualmente en SAP"]
    G --> H["Se confirma pago\npor correo al empleado"]
```

### Problemas identificados

| Problema | Impacto |
|----------|---------|
| Solicitudes por correo y Excel | No hay trazabilidad de estados, demoras ni responsables |
| Aprobaciones por correo | Sin registro de auditoria, sin SLAs, sin control de quien aprobo y cuando |
| Documentacion manual | Errores frecuentes en resoluciones, formatos de anticipo y clausulas de confidencialidad |
| Legalizacion en formatos dispersos | Excel, fotos, escaneos con inconsistencias que retrasan cierres contables |
| Notificacion de pago por correo | Conciliacion manual entre lo aprobado y lo efectivamente girado |
| Sin clasificacion legal | No se discriminan categorias de gasto, riesgo de tratamiento salarial incorrecto (Art. 130 CST) |

---

## 2. Flujo TO-BE (Solucion Propuesta)

La solucion digitaliza el proceso completo con orquestacion en Power Automate y datos centralizados en Dataverse:

```mermaid
flowchart TD
    A["Empleado crea solicitud\nen Power Apps"] --> B["Clasifica tipo de viatico\nOcasional o Permanente"]
    B --> C["Desglosa gastos por categoria\nHospedaje, Alimentacion,\nTransporte, Representacion"]
    C --> D["Adjunta soportes\nen Dataverse"]
    D --> E["Power Automate valida\ncampos, topes y desglose legal"]
    E --> F{"Pasa validacion?"}
    F -->|No| G["Devuelve al empleado\ncon detalle de errores"]
    F -->|Si| H["Aprobacion Nivel 1\nJefe Inmediato"]
    H --> I{"Decision del jefe?"}
    I -->|Rechazado| J["Registra motivo obligatorio\nNotifica al empleado"]
    I -->|Aprobado| K["Aprobacion Nivel 2\nGestion Humana"]
    K --> L{"Decision de GH?"}
    L -->|Rechazado| J
    L -->|Aprobado| M["Genera instruccion de pago\nen tablas SAP simuladas"]
    M --> N["Notifica a Finanzas\npara ejecucion de pago"]
    N --> O["Finanzas confirma pago\nen el sistema"]
    O --> P["Estado: Pagada\nNotifica al empleado"]
```

### Mejoras logradas

| Aspecto | AS-IS | TO-BE |
|---------|-------|-------|
| Solicitud | Correo + Excel | Formulario Power Apps con validaciones |
| Clasificacion legal | Inexistente | Obligatoria (Art. 130 CST) |
| Aprobaciones | Por correo, sin registro | Power Automate con auditoria automatica |
| Trazabilidad | Nula | Completa en tabla de auditoria |
| Notificaciones | Manuales por correo | Automaticas en cada hito |
| Pago | Proceso manual en SAP | Instruccion automatica via tablas OData |
| Conciliacion | Manual, propenso a errores | Cruce automatizado de anticipos y tarjetas |
| Seguridad | Sin control de acceso | RBAC por rol con Azure AD |
