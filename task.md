# Tareas de Implementacion - MVP Viaticos

## Fase 1: Infraestructura y DevOps (Semana 1-2)

### 1.1 Azure DevOps
- [x] Crear proyecto Azure DevOps "Viaticos-BanRep"
- [x] Configurar Boards con EPICs y HUs del backlog
- [x] Crear repositorio Git con estructura de carpetas del proyecto
- [x] Push inicial de toda la documentacion (/docs/)

### 1.2 Pipelines CI/CD
- [x] Crear `despliegue/pipelines/export-solution.yml` (exportar solucion managed de Dev)
- [x] Crear `despliegue/pipelines/import-to-test.yml` (importar a ambiente Test)
- [x] Crear `despliegue/pipelines/import-to-prod.yml` (importar a Prod con gate de aprobacion)
- [x] Crear `despliegue/checklist.md` (checklist de despliegue)
- [x] Crear `despliegue/rollback.md` (procedimiento de rollback)

### 1.3 Power Platform Setup
- [x] Registrar Power Apps Developer Plan
- [x] Crear ambiente de desarrollo en Dataverse
- [x] Crear solucion managed "ViaticosApp"
- [x] Instalar Power Platform CLI (pac)

---

## Fase 2: Modelo de Datos en Dataverse (Semana 2)

### 2.1 Definiciones de tablas (JSON schemas)
- [x] Crear `solucion/dataverse/tablas/solicitudes.json` (definicion de campos, tipos, relaciones)
- [x] Crear `solucion/dataverse/tablas/detalle_gastos.json`
- [x] Crear `solucion/dataverse/tablas/aprobaciones.json`
- [x] Crear `solucion/dataverse/tablas/pagos.json`
- [x] Crear `solucion/dataverse/tablas/documentos.json`
- [x] Crear `solucion/dataverse/tablas/auditoria.json`

### 2.2 Tablas SAP simuladas
- [x] Crear `solucion/dataverse/sap_simulado/sap_instruccion_pago.json`
- [x] Crear `solucion/dataverse/sap_simulado/sap_confirmacion_pago.json`
- [x] Crear `solucion/dataverse/sap_simulado/sap_maestro_empleados.json`
- [x] Crear `solucion/dataverse/sap_simulado/sap_centros_costo.json`

### 2.3 Tablas de configuracion
- [x] Crear `solucion/dataverse/configuracion/config_topes_monto.json`
- [x] Crear `solucion/dataverse/configuracion/config_niveles_aprobacion.json`
- [x] Crear `solucion/dataverse/configuracion/config_categorias_gasto.json`
- [x] Crear `solucion/dataverse/configuracion/config_estados_transicion.json`
- [x] Crear `solucion/dataverse/configuracion/config_tipos_documento.json`

### 2.4 Datos iniciales (CSV para importar)
- [x] Crear `solucion/dataverse/configuracion/datos/topes_monto.csv`
- [x] Crear `solucion/dataverse/configuracion/datos/niveles_aprobacion.csv`
- [x] Crear `solucion/dataverse/configuracion/datos/categorias_gasto.csv`
- [x] Crear `solucion/dataverse/configuracion/datos/estados_transicion.csv`
- [x] Crear `solucion/dataverse/configuracion/datos/tipos_documento.csv`
- [x] Crear `solucion/dataverse/sap_simulado/datos/maestro_empleados.csv` (datos de prueba)
- [x] Crear `solucion/dataverse/sap_simulado/datos/centros_costo.csv` (datos de prueba)

### 2.5 Reglas de negocio
- [x] Crear `solucion/dataverse/reglas/solicitud_validaciones.md` (documentacion de reglas)
- [x] Crear `solucion/dataverse/reglas/calculo_incidencia_salarial.md`

### 2.6 Roles de seguridad
- [x] Crear `solucion/dataverse/roles/rol_empleado.json`
- [x] Crear `solucion/dataverse/roles/rol_jefe.json`
- [x] Crear `solucion/dataverse/roles/rol_gh.json`
- [x] Crear `solucion/dataverse/roles/rol_finanzas.json`
- [x] Crear `solucion/dataverse/roles/rol_admin.json`

---

## Fase 3: Power Apps (Semana 3)

### 3.1 Documentacion de pantallas
- [x] Crear `solucion/power_apps/pantallas.md` (especificacion de cada pantalla y componentes)
- [x] Crear `solucion/power_apps/navegacion.md` (mapa de navegacion entre pantallas)

---

## Fase 4: Power Automate (Semana 3-4)

### 4.1 Definiciones de flujos
- [x] Crear `solucion/power_automate/flujo_solicitud/definicion.md` (trigger, acciones, condiciones)
- [x] Crear `solucion/power_automate/flujo_aprobacion/definicion.md`
- [x] Crear `solucion/power_automate/flujo_pago/definicion.md`
- [x] Crear `solucion/power_automate/flujo_notificaciones/definicion.md`
- [x] Crear `solucion/power_automate/flujo_auditoria/definicion.md`
- [x] Crear `solucion/power_automate/flujo_notificaciones/plantillas_correo.md` (plantillas HTML)

---

## Fase 5: Pruebas y Despliegue (Semana 5-6)

### 5.1 Casos de prueba
- [x] Crear `pruebas/casos/TC-SOL_solicitudes.md`
- [x] Crear `pruebas/casos/TC-APR_aprobaciones.md`
- [x] Crear `pruebas/casos/TC-PAG_pagos.md`
- [x] Crear `pruebas/casos/TC-SEG_seguridad.md`
- [x] Crear `pruebas/casos/TC-E2E_integracion.md`
- [x] Crear `pruebas/uat/checklist_uat.md`
