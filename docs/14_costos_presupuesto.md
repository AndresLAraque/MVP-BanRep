# Costos y Presupuesto - MVP Sistema de Viaticos

## 1. Supuestos Generales

| Parametro | Valor supuesto | Nota |
|-----------|---------------|------|
| Duracion del proyecto | 8 semanas (2 meses) | Incluye descubrimiento hasta estabilizacion |
| Tamano del equipo | 5 personas | Core team |
| TRM (Tasa de cambio) | $4.200 COP por 1 USD | Supuesto para conversiones |
| Usuarios del sistema en produccion | 200 empleados, 30 jefes, 8 GH, 5 finanzas, 3 admin | Total: ~246 usuarios |
| Horario laboral | 8 horas/dia, 22 dias/mes | Estandar Colombia |
| Ubicacion del equipo | Bogota, Colombia | Trabajo hibrido |

---

## 2. Costos de Personal (Desarrollo e Implementacion)

### 2.1 Equipo core

| Rol | Cantidad | Dedicacion | Salario mensual (COP) | Meses | Costo total (COP) |
|-----|----------|-----------|----------------------|-------|-------------------|
| Arquitecto de soluciones Power Platform | 1 | 100% | $15.000.000 | 2 | $30.000.000 |
| Desarrollador Power Platform Senior | 1 | 100% | $12.000.000 | 2 | $24.000.000 |
| Desarrollador Power Platform Junior | 1 | 100% | $7.000.000 | 2 | $14.000.000 |
| Analista funcional / Product Owner | 1 | 100% | $10.000.000 | 2 | $20.000.000 |
| QA / Tester | 1 | 50% S1-S4, 100% S5-S8 | $6.000.000 | 2 | $12.000.000 |
| **Subtotal personal desarrollo** | | | | | **$100.000.000** |

### 2.2 Personal de soporte (parcial)

| Rol | Cantidad | Dedicacion | Salario mensual (COP) | Meses | Costo total (COP) |
|-----|----------|-----------|----------------------|-------|-------------------|
| Especialista SAP Basis (consultoria) | 1 | 20% | $18.000.000 | 1 | $3.600.000 |
| Administrador Azure AD / TI | 1 | 10% | $10.000.000 | 2 | $2.000.000 |
| Abogado laboral / Legal (consultoria) | 1 | 10% | $12.000.000 | 0.5 | $600.000 |
| **Subtotal personal soporte** | | | | | **$6.200.000** |

### Total costos de personal: $106.200.000 COP (~$25.286 USD)

---

## 3. Costos de Licenciamiento

### 3.1 Fase de desarrollo y demo (Free Tier)

| Componente | Plan | Costo mensual | Meses | Total |
|-----------|------|--------------|-------|-------|
| Power Apps | Developer Plan | $0 | 2 | $0 |
| Power Automate | Incluido en Developer Plan | $0 | 2 | $0 |
| Dataverse | Incluido en Developer Plan | $0 | 2 | $0 |
| Azure DevOps | Free Tier (5 usuarios) | $0 | 2 | $0 |
| **Total fase demo** | | | | **$0** |

### 3.2 Fase de produccion (estimacion anual)

| Componente | Plan | Usuarios | Costo/usuario/mes (USD) | Costo anual (USD) | Costo anual (COP) |
|-----------|------|----------|------------------------|------------------|-------------------|
| Power Apps | Per-app (1 app) | 246 | $5 | $14.760 | $61.992.000 |
| Power Automate | Per-user with attended RPA | 10 (GH+Fin+Admin) | $15 | $1.800 | $7.560.000 |
| Dataverse | Capacidad adicional (1 GB) | 1 | $40/mes | $480 | $2.016.000 |
| Azure DevOps | Basic (si crecen a mas de 5) | 5 | $0 | $0 | $0 |
| **Total produccion anual** | | | | **$17.040** | **$71.568.000** |

**Alternativa Power Apps per-user (acceso ilimitado a apps):**

| Componente | Plan | Usuarios | Costo/usuario/mes (USD) | Costo anual (USD) | Costo anual (COP) |
|-----------|------|----------|------------------------|------------------|-------------------|
| Power Apps + Power Automate | Per-user | 246 | $20 | $59.040 | $247.968.000 |

La opcion per-app es significativamente mas economica si solo se usa una aplicacion.

---

## 4. Costos de Infraestructura

| Concepto | Descripcion | Costo (COP) |
|----------|------------|-------------|
| Ambiente de desarrollo | Incluido en Developer Plan | $0 |
| Ambiente de pruebas | Incluido en Developer Plan (segundo ambiente) | $0 |
| Ambiente de produccion | Requiere tenant con licencias de produccion | Incluido en licenciamiento |
| Almacenamiento adicional Dataverse | Si se exceden los 10 GB base | ~$168.000/mes por GB adicional |
| Azure subscription (para DevOps billing) | Vinculacion basica sin consumo | $0 |

---

## 5. Costos de Capacitacion

| Concepto | Detalle | Costo (COP) |
|----------|---------|-------------|
| Preparacion de materiales | 3 guias rapidas, 3 videos, manual de admin | Incluido en personal de desarrollo |
| Sesiones de capacitacion | 15 sesiones de 1.5-3 horas | Incluido en personal de desarrollo |
| Sala de reuniones / Teams | 15 sesiones | $0 (infraestructura existente) |
| Tiempo de usuarios en capacitacion | 246 usuarios x 2 horas promedio = 492 horas-hombre | $12.300.000 (costo de oportunidad) |
| **Total capacitacion** | | **$12.300.000** |

---

## 6. Costos de Operacion Anual (Post-MVP)

| Concepto | Descripcion | Costo anual (COP) |
|----------|------------|-------------------|
| Licenciamiento Power Platform | Per-app + Power Automate + Dataverse | $71.568.000 |
| Administrador funcional (parcial) | 20% del tiempo de 1 persona | $24.000.000 |
| Soporte N2 (parcial) | 10% del tiempo de 1 desarrollador | $14.400.000 |
| Mejoras y evolutivos | 2 sprints por ano de 2 semanas | $24.000.000 |
| **Total operacion anual** | | **$133.968.000** |

---

## 7. Resumen de Inversion

| Concepto | Costo (COP) | Costo (USD) |
|----------|------------|-------------|
| Desarrollo e implementacion (8 semanas) | $106.200.000 | $25.286 |
| Licenciamiento fase demo | $0 | $0 |
| Capacitacion | $12.300.000 | $2.929 |
| **Total inversion inicial** | **$118.500.000** | **$28.214** |
| Operacion anual (ano 1 en adelante) | $133.968.000 | $31.897 |

---

## 8. Cronograma de Pagos

| Mes | Concepto | Monto (COP) |
|-----|---------|------------|
| Mes 1 | Personal desarrollo + soporte (50%) | $56.200.000 |
| Mes 2 | Personal desarrollo + soporte (50%) + capacitacion | $62.300.000 |
| Mes 3+ | Licenciamiento produccion (mensual) | $5.964.000/mes |
| Mes 3+ | Operacion y soporte (mensual) | $5.200.000/mes |

Todos los montos son supuestos basados en tarifas de mercado colombiano (2026) y estan sujetos a validacion con el area financiera del Banco de la Republica.
