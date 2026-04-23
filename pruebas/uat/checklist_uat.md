# Casos de Prueba: Seguridad RBAC (TC-SEG)

| ID | Descripcion | Usuario de Prueba | Pasos | Resultado Esperado |
|----|-------------|-------------------|-------|-------------------|
| TC-SEG-01 | Acceso Solicitante | Rol: Empleado | Intentar entrar a la Consola de Aprobacion. | El sistema debe denegar el acceso o redirigir al Dashboard. |
| TC-SEG-02 | Visibilidad de Datos | Rol: Empleado | Intentar ver una solicitud que no fue creada por el. | Dataverse debe filtrar los registros y no mostrar solicitudes ajenas. |
| TC-SEG-03 | Privilegios de Admin | Rol: Admin | Modificar un tope de monto en CONFIG_TOPES_MONTO. | Accion permitida. El cambio debe reflejarse inmediatamente en nuevas solicitudes. |

---

# Casos de Prueba: Fin a Fin (TC-E2E)

| Fase | Accion | Actor | Validacion |
|------|--------|-------|------------|
| 1 | Crear solicitud completa | Empleado | Registro en Dataverse + Correo de bienvenida. |
| 2 | Aprobacion Tecnica | Jefe | Estado: 'Aprobada Jefe' + Alerta Teams a GH. |
| 3 | Aprobacion Legal | GH | Estado: 'Aprobada GH' + Disparo de flujo SAP. |
| 4 | Instruccion Pago | Sistema | Escritura en sap_instruccion_pago. |
| 5 | Confirmacion Pago | Finanzas/SAP | Estado: 'Pagada' + Notificacion final al empleado. |

---

# Checklist de Aceptacion de Usuario (UAT)

- [ ] ¿El formulario valida los montos segun los topes de la ciudad?
- [ ] ¿Se genera la incidencia salarial correcta segun el Art. 130 CST?
- [ ] ¿Llegan las notificaciones a Teams y Correo en tiempo real?
- [ ] ¿Es posible adjuntar y visualizar archivos PDF/JPG?
- [ ] ¿El historial de auditoria muestra todos los niveles de aprobacion?
- [ ] ¿El diseño Azul/Oro es consistente en todas las pantallas y correos?
