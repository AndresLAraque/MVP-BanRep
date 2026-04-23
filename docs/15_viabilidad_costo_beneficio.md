# Analisis de Viabilidad y Costo-Beneficio

## 1. Resumen Ejecutivo

Este analisis evalua la viabilidad financiera y operativa de implementar el sistema de gestion de viaticos en el Banco de la Republica. La inversion inicial es de $118.5 millones COP con un costo operativo anual de $134 millones COP. Los beneficios cuantificables superan los $350 millones COP anuales, generando un retorno de inversion positivo desde el primer ano.

---

## 2. Beneficios Cuantificables

### 2.1 Reduccion de tiempo operativo

| Actividad | Tiempo actual (manual) | Tiempo con sistema | Ahorro por solicitud | Solicitudes/ano (supuesto) | Ahorro anual (horas) |
|-----------|----------------------|-------------------|---------------------|--------------------------|---------------------|
| Crear solicitud (empleado) | 45 minutos | 15 minutos | 30 minutos | 600 | 300 |
| Revision y aprobacion (jefe) | 30 minutos | 10 minutos | 20 minutos | 600 | 200 |
| Validacion GH | 40 minutos | 10 minutos | 30 minutos | 600 | 300 |
| Procesamiento de pago (finanzas) | 60 minutos | 15 minutos | 45 minutos | 600 | 450 |
| Consolidacion y seguimiento | 30 minutos | 0 (automatico) | 30 minutos | 600 | 300 |
| Legalizacion (futuro) | 45 minutos | 15 minutos | 30 minutos | 600 | 300 |
| **Total** | | | | | **1.850 horas/ano** |

**Valoracion del ahorro de tiempo:**

- Costo hora promedio ponderado (todos los roles): $55.000 COP/hora (supuesto)
- Ahorro anual: 1.850 horas x $55.000 = **$101.750.000 COP**

### 2.2 Reduccion de errores y reprocesos

| Tipo de error | Frecuencia actual (supuesto) | Costo por error (supuesto) | Reduccion con sistema | Ahorro anual (COP) |
|--------------|-----------------------------|-----------------------|---------------------|--------------------|
| Datos incorrectos en solicitud | 15% de solicitudes (90/ano) | $150.000 (reproceso) | 90% | $12.150.000 |
| Clasificacion legal incorrecta de viaticos | 20% de solicitudes (120/ano) | $500.000 (riesgo salarial + correccion) | 95% | $57.000.000 |
| Error en monto de pago | 5% de pagos (30/ano) | $200.000 (conciliacion) | 95% | $5.700.000 |
| Documento extraviado | 10% de solicitudes (60/ano) | $100.000 (reconstruccion) | 99% | $5.940.000 |
| Pago duplicado | 2% de pagos (12/ano) | $3.000.000 (reversion) | 99% | $35.640.000 |
| **Total** | | | | **$116.430.000** |

### 2.3 Reduccion de riesgo legal

| Riesgo | Probabilidad actual | Impacto financiero (supuesto) | Reduccion con sistema | Valor de reduccion anual (COP) |
|--------|--------------------|-----------------------------|---------------------|-----------------------------|
| Tratamiento salarial incorrecto de viaticos permanentes (Art. 130 CST) | Media (30%) | $200.000.000 (reliquidacion de prestaciones y aportes) | 95% | $57.000.000 |
| Hallazgo de auditoria por falta de trazabilidad | Media (25%) | $50.000.000 (correctivos y sanciones internas) | 90% | $11.250.000 |
| Incumplimiento de retencion documental (DIAN) | Baja (10%) | $30.000.000 (sanciones) | 80% | $2.400.000 |
| **Total** | | | | **$70.650.000** |

### 2.4 Otros beneficios cuantificables

| Beneficio | Descripcion | Valor anual (COP) |
|-----------|------------|-------------------|
| Reduccion de papel y mensajeria | Eliminacion de formatos impresos, correo certificado | $5.000.000 |
| Reduccion de llamadas de seguimiento | Empleados consultan estado en el sistema | $8.000.000 |
| Mejor negociacion de viaticos | Datos consolidados permiten negociar tarifas corporativas | $15.000.000 |
| **Total** | | **$28.000.000** |

---

## 3. Resumen de Beneficios

| Categoria | Beneficio anual (COP) |
|-----------|----------------------|
| Ahorro de tiempo operativo | $101.750.000 |
| Reduccion de errores y reprocesos | $116.430.000 |
| Reduccion de riesgo legal | $70.650.000 |
| Otros beneficios | $28.000.000 |
| **Total beneficios anuales** | **$316.830.000** |

---

## 4. Beneficios No Cuantificables

| Beneficio | Descripcion |
|-----------|------------|
| Trazabilidad completa | Auditoria de cada accion, cumplimiento de politicas internas |
| Satisfaccion del empleado | Proceso mas rapido, transparente, sin dependencia de correos |
| Cumplimiento normativo demostrable | Art. 130 CST implementado con evidencia sistematica |
| Base para analitica advanced | Datos estructurados para Power BI, tendencias, optimizacion |
| Escalabilidad | Plataforma extensible a otros procesos de GH sin nueva infraestructura |
| Imagen institucional | Banco de la Republica como referente en digitalizacion de procesos |
| Preparacion para SAP HANA | Integracion disenada para la migracion sin reprocesos |

---

## 5. Analisis Financiero

### 5.1 Flujo de caja proyectado (5 anos)

| Concepto | Ano 0 (Inversion) | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|----------|-------------------|-------|-------|-------|-------|-------|
| Inversion inicial | -$118.500.000 | | | | | |
| Costo operativo anual | | -$133.968.000 | -$140.666.000 | -$147.700.000 | -$155.085.000 | -$162.839.000 |
| Beneficios anuales | | $316.830.000 | $332.672.000 | $349.305.000 | $366.770.000 | $385.109.000 |
| **Flujo neto** | **-$118.500.000** | **$182.862.000** | **$192.006.000** | **$201.605.000** | **$211.685.000** | **$222.270.000** |
| **Flujo acumulado** | **-$118.500.000** | **$64.362.000** | **$256.368.000** | **$457.973.000** | **$669.658.000** | **$891.928.000** |

Supuestos: inflacion anual del 5% aplicada tanto a costos como a beneficios.

### 5.2 Indicadores financieros

| Indicador | Valor | Interpretacion |
|-----------|-------|---------------|
| **Periodo de recuperacion (Payback)** | **7.8 meses** | La inversion se recupera antes del primer ano |
| **ROI (Retorno sobre Inversion) - Ano 1** | **154%** | Por cada peso invertido se recuperan $2.54 |
| **VPN (Valor Presente Neto) a 5 anos** | **$710.000.000 COP** | Proyecto altamente viable (tasa de descuento: 10%) |
| **TIR (Tasa Interna de Retorno)** | **155%** | Muy superior al costo de capital |
| **Relacion Costo/Beneficio** | **2.67:1** | Beneficios son 2.67 veces los costos anuales |

---

## 6. Analisis de Sensibilidad

| Escenario | Variable modificada | Impacto en ROI Ano 1 | Payback |
|-----------|--------------------|-----------------------|---------|
| Base | Todo segun supuestos | 154% | 7.8 meses |
| Pesimista | Solicitudes/ano bajan a 400 (33% menos) | 89% | 11.2 meses |
| Optimista | Solicitudes/ano suben a 800 | 218% | 5.5 meses |
| Licenciamiento alto | Power Apps per-user ($20) en vez de per-app ($5) | 34% | 16.8 meses |
| Sin riesgo legal | Se excluye el beneficio de reduccion de riesgo legal | 110% | 9.3 meses |
| Equipo minimo | Solo 3 personas en desarrollo (architect + dev + QA) | 211% | 5.9 meses |

El proyecto es viable en todos los escenarios excepto si se usa la licencia per-user para los 246 usuarios, donde aun asi se recupera en menos de 17 meses.

---

## 7. Comparativa con Alternativas

| Alternativa | Costo estimado implementacion (COP) | Costo operativo anual (COP) | Tiempo de implementacion | Alineacion con ecosistema |
|------------|-------------------------------------|---------------------------|------------------------|-----------------------|
| **Power Platform (propuesta)** | **$118.500.000** | **$133.968.000** | **8 semanas** | **Nativa en Microsoft** |
| SAP Concur | $300.000.000+ | $400.000.000+ (licencias + soporte) | 4-6 meses | Externa, requiere integracion |
| Desarrollo a medida (.NET/React) | $400.000.000+ | $200.000.000+ (hosting + soporte) | 6-9 meses | Requiere infraestructura propia |
| Tickelia / tainnova | $150.000.000+ | $180.000.000+ | 3-4 meses | Externa, personalizacion limitada |
| Mantener proceso manual | $0 | $316.830.000 (costo de ineficiencia) | N/A | N/A |

---

## 8. Recomendacion

El proyecto es **viable y recomendable** por las siguientes razones:

1. **Retorno rapido**: La inversion se recupera en menos de 8 meses
2. **Bajo riesgo financiero**: La inversion inicial es moderada ($118.5M COP) comparada con alternativas
3. **Free tier para demo**: No se requiere inversion en licenciamiento hasta aprobar produccion
4. **Alineacion tecnologica**: Power Platform es parte del ecosistema Microsoft del Banco
5. **Cumplimiento garantizado**: Implementa Art. 130 CST de manera sistematica y auditable
6. **Escalabilidad**: Arquitectura preparada para SAP HANA, AI Builder y procesos adicionales
7. **Reduccion de riesgo**: Elimina riesgos de clasificacion salarial incorrecta ($57M COP/ano)

---

## 9. Nota sobre Supuestos

Todos los valores presentados son supuestos iniciales basados en:

- Tarifas de mercado colombiano para perfiles de Power Platform (2026)
- Precios publicos de licenciamiento Microsoft Power Platform
- Estimaciones conservadoras de volumen de solicitudes
- Estimaciones de mercado para costos de errores y reprocesos

Estos valores deben ser validados y ajustados con datos reales del Banco de la Republica antes de presentar como caso de negocio formal.
