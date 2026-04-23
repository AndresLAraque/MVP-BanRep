# Plan de Capacitacion - MVP Sistema de Viaticos

## 1. Objetivo

Garantizar que todos los usuarios del sistema de viaticos adquieran las competencias necesarias para operar la solucion de manera autonoma, segun su rol, dentro de las primeras 2 semanas posteriores al despliegue.

---

## 2. Poblacion Objetivo

| Grupo | Rol en el sistema | Cantidad estimada | Nivel de complejidad |
|-------|-------------------|-------------------|---------------------|
| Empleados solicitantes | Empleado | 150-200 personas | Basico |
| Jefes inmediatos | Jefe / Aprobador N1 | 25-30 personas | Basico-Medio |
| Personal de Gestion Humana | GH / Aprobador N2 | 5-8 personas | Medio |
| Personal de Finanzas/Pagos | Finanzas | 3-5 personas | Medio |
| Administradores funcionales | Admin | 2-3 personas | Avanzado |
| Equipo de soporte TI | Soporte | 2-3 personas | Avanzado |

---

## 3. Metodologia

| Metodo | Aplicacion | Herramientas |
|--------|-----------|-------------|
| Sesiones presenciales/virtuales | Capacitacion inicial por grupo de rol | Microsoft Teams, sala de reuniones |
| Videos tutoriales | Material de referencia permanente, accesible bajo demanda | Grabaciones en Teams, repositorio interno |
| Guias rapidas | Documentos de 1-2 paginas con pasos principales por rol | PDF distribuido por correo y publicado en intranet |
| Ambiente de practica | Ejercicios con datos de prueba en ambiente Test | Ambiente Dataverse de pruebas |
| Soporte post-capacitacion | Canal de soporte para dudas durante las primeras 4 semanas | Canal de Teams dedicado |

---

## 4. Contenido por Rol

### 4.1 Empleado (2 horas)

| Modulo | Duracion | Contenido |
|--------|----------|----------|
| Introduccion | 15 min | Que es el sistema, por que se implementa, beneficios |
| Crear solicitud | 30 min | Formulario, campos obligatorios, tipos de viatico, desglose de gastos |
| Adjuntar documentos | 15 min | Tipos de archivo, tamano maximo, vinculacion a solicitud |
| Consultar estado | 15 min | Mis Solicitudes, timeline, indicador de progreso |
| Notificaciones | 10 min | Que correos recibira y cuando |
| Practica guiada | 30 min | Crear solicitud completa en ambiente de pruebas |
| Preguntas | 15 min | Resolucion de dudas |

### 4.2 Jefe/Aprobador (1.5 horas)

| Modulo | Duracion | Contenido |
|--------|----------|----------|
| Introduccion | 10 min | Responsabilidades como aprobador nivel 1 |
| Aprobar solicitudes | 20 min | Revision de solicitud, desglose, documentos. Aprobar o rechazar |
| Rechazo con comentario | 15 min | Politica de comentario obligatorio, buenas practicas |
| Vista de equipo | 15 min | Como ver solicitudes de su equipo directo |
| Practica guiada | 20 min | Aprobar y rechazar solicitudes en ambiente de pruebas |
| Preguntas | 10 min | Resolucion de dudas |

### 4.3 Gestion Humana (2 horas)

| Modulo | Duracion | Contenido |
|--------|----------|----------|
| Marco legal Art. 130 CST | 20 min | Clasificacion de viaticos, incidencia salarial, criterios del Ministerio |
| Aprobacion nivel 2 | 20 min | Revision de solicitudes aprobadas por jefe, validacion de politica |
| Alertas de incidencia salarial | 15 min | Que hacer cuando el sistema genera alerta por viatico permanente |
| Consulta y auditoria | 15 min | Ver historial completo, filtros, exportacion |
| Reportes | 15 min | Metricas de solicitudes, tiempos, costos por area |
| Practica guiada | 25 min | Flujo E2E completo en ambiente de pruebas |
| Preguntas | 10 min | Resolucion de dudas |

### 4.4 Finanzas (1.5 horas)

| Modulo | Duracion | Contenido |
|--------|----------|----------|
| Instrucciones de pago | 20 min | Como llegan las instrucciones, que datos contienen |
| Confirmacion de pago | 20 min | Proceso de confirmacion en el sistema y en SAP |
| Conciliacion | 20 min | Tarjetas corporativas vs anticipos, cruce de informacion |
| Auditoria de pagos | 15 min | Trazabilidad de pagos, referencias SAP |
| Practica guiada | 15 min | Confirmar pagos en ambiente de pruebas |

### 4.5 Administrador (3 horas)

| Modulo | Duracion | Contenido |
|--------|----------|----------|
| Arquitectura del sistema | 20 min | Componentes, flujos, datos |
| Configuracion de topes | 20 min | Tabla CONFIG_TOPES_MONTO: agregar, modificar, desactivar |
| Configuracion de niveles de aprobacion | 20 min | Tabla CONFIG_NIVELES_APROBACION |
| Gestion de categorias y estados | 15 min | Tablas de catalogo |
| Gestion de usuarios y roles | 20 min | Azure AD, grupos de seguridad, mapeo a Dataverse |
| Monitoreo de flujos | 20 min | Centro de administracion de Power Automate, errores comunes |
| Tablas SAP simuladas | 15 min | Estructura, datos de prueba, preparacion para migracion |
| Resolucion de problemas | 20 min | Escenarios comunes: flujo atascado, error de pago, usuario sin acceso |

---

## 5. Cronograma de Capacitacion

| Semana | Actividad | Grupo | Formato |
|--------|----------|-------|---------|
| S6 (Despliegue) | Capacitacion de administradores | Admin + Soporte TI | Presencial (3h) |
| S6 | Capacitacion de GH y Finanzas | GH + Finanzas | Presencial (2h) |
| S6 | Capacitacion de jefes aprobadores | Jefes (3 sesiones de 10 personas) | Virtual (1.5h) |
| S6-S7 | Capacitacion de empleados | Empleados (10 sesiones de 20 personas) | Virtual (2h) |
| S6 | Publicacion de guias rapidas y videos | Todos | Intranet + correo |
| S7-S8 | Soporte post-capacitacion activo | Todos | Canal de Teams |

---

## 6. Evaluacion de Efectividad

| Indicador | Meta | Metodo |
|-----------|------|--------|
| Asistencia a capacitacion | 95% de usuarios por rol | Registro de asistencia |
| Evaluacion de comprension | Mayor o igual a 80% de respuestas correctas | Quiz de 10 preguntas al finalizar |
| Solicitudes creadas sin errores en primera semana | Mayor o igual a 85% | Monitoreo de validaciones fallidas |
| Tickets de soporte en primera semana | Menor a 20 | Conteo en canal de Teams |
| Satisfaccion de la capacitacion | Mayor o igual a 4/5 | Encuesta post-sesion |

---

## 7. Materiales de Capacitacion

| Material | Formato | Responsable | Ubicacion |
|----------|---------|-------------|-----------|
| Guia rapida: Empleado | PDF, 2 paginas | Desarrollador + QA | Intranet, correo |
| Guia rapida: Aprobador | PDF, 1 pagina | Desarrollador + QA | Intranet, correo |
| Guia rapida: Finanzas | PDF, 1 pagina | Desarrollador + QA | Intranet, correo |
| Manual de administracion | PDF, 15 paginas | Desarrollador | /docs/ |
| Video: Crear solicitud paso a paso | Video 5 min | Desarrollador | Intranet |
| Video: Aprobar solicitud | Video 3 min | Desarrollador | Intranet |
| Video: Configurar topes | Video 3 min | Desarrollador | Intranet |
| Ambiente de practica con datos de prueba | Ambiente Test | TI | Dataverse Test |
