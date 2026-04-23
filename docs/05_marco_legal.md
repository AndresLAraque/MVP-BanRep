# Marco Legal - Viaticos en Colombia

## 1. Base Normativa

### Articulo 130 del Codigo Sustantivo del Trabajo (CST)

El Articulo 130 del CST establece las reglas para el tratamiento de los viaticos en la relacion laboral colombiana. Define dos tipos de viaticos segun su frecuencia y naturaleza, y establece cuales constituyen salario.

**Texto relevante del articulo:**

> "Los viaticos permanentes constituyen salario en aquella parte destinada a proporcionar al trabajador manutension y alojamiento; pero no en lo que solo tenga por finalidad proporcionar los medios de transporte o los gastos de representacion. Los viaticos accidentales no constituyen salario en ningun caso."

---

## 2. Clasificacion de Viaticos

### 2.1 Viaticos Accidentales (Ocasionales)

Son aquellos que se otorgan con motivo de un requerimiento extraordinario, no habitual y poco frecuente. No forman parte de la actividad ordinaria del cargo del trabajador.

**Criterios para determinar ocasionalidad:**
- La actividad que origina el viaje no es parte esencial de las funciones del cargo
- El desplazamiento es infrecuente e irregular
- No existe un patron temporal predecible
- Los viajes son cortos y esporadicos

**Tratamiento:** No constituyen salario bajo ninguna circunstancia, independientemente de la categoria de gasto que cubran.

### 2.2 Viaticos Permanentes

Son aquellos destinados a cubrir gastos derivados de un requerimiento laboral ordinario, habitual y frecuente. Los desplazamientos son parte inherente de las funciones del cargo.

**Criterios para determinar permanencia (Ministerio de Trabajo):**

| Criterio | Descripcion | Indicador en el sistema |
|----------|------------|----------------------|
| Habitualidad | Los viajes son frecuentes para el cargo | Frecuencia calculada: numero de viajes por periodo por empleado |
| Periodicidad | Existe un patron temporal regular | Analisis de fechas historicas de solicitudes anteriores |
| Funciones del cargo | El viaje es parte esencial de las funciones | Campo motivo_viaje vinculado al perfil del cargo |
| Regularidad | Los montos y destinos son consistentes | Comparacion con historico de solicitudes previas del empleado |
| Naturaleza de la labor | La actividad pertenece al core del negocio o es extraordinaria | Clasificacion por el solicitante con validacion de GH |

**Tratamiento salarial diferenciado por categoria:**

| Categoria de gasto | Constituye salario | Incide en prestaciones | Base legal |
|--------------------|--------------------|----------------------|-----------|
| Hospedaje (alojamiento) | Si | Cesantias, prima de servicios, vacaciones, seguridad social, parafiscales | Art. 130 CST |
| Alimentacion (manutencion) | Si | Cesantias, prima de servicios, vacaciones, seguridad social, parafiscales | Art. 130 CST |
| Transporte (medios de desplazamiento) | No | No aplica | Art. 130 CST |
| Gastos de representacion | No | No aplica. Es gasto contable de la empresa, no ingreso del trabajador | Art. 130 CST |

---

## 3. Jurisprudencia Relevante

### Corte Suprema de Justicia

La Corte Suprema de Justicia ha establecido en su jurisprudencia (incluyendo sentencias reiteradas hasta 2021) que:

1. **Obligacion de discriminar:** Si el empleador no discrimina los viaticos por categoria (hospedaje, alimentacion, transporte, representacion), la totalidad del viatico permanente se considera constitutivo de salario. Esto implica un costo significativamente mayor para la empresa en terminos de prestaciones sociales y aportes.

2. **Carga de la prueba:** Le corresponde al empleador demostrar la naturaleza ocasional de los viaticos. Si no puede demostrarlo, se presumen permanentes.

3. **Criterio funcional sobre el formal:** No basta con que el empleador denomine los viaticos como "ocasionales"; lo determinante es la realidad de la prestacion del servicio y la frecuencia de los desplazamientos.

---

## 4. Efecto Tributario

Los viaticos tienen impacto tributario para el trabajador:

- Los pagos que constituyen salario son ingresos del trabajador y deben incluirse en los certificados de ingresos y retenciones
- Los gastos de representacion, al ser gastos de la empresa, no entran al patrimonio del trabajador
- Los anticipos entregados y no legalizados generan obligaciones contables que deben resolverse

---

## 5. Consideraciones para Tarjetas Corporativas

| Medio de pago | Naturaleza | Tratamiento |
|--------------|-----------|-------------|
| Tarjeta corporativa | Gasto de la empresa directamente | Los gastos pagados con tarjeta corporativa son gastos de representacion o gastos directos de la empresa. No constituyen ingreso del trabajador |
| Anticipo en efectivo | Dinero entregado al trabajador | Debe legalizarse con soportes. La diferencia no legalizada puede generar obligaciones para el trabajador |
| Reembolso posterior | Pago al trabajador despues del viaje | Debe clasificarse por categoria para determinar tratamiento salarial |

### Conciliacion

- Tarjetas corporativas: se concilian contra el extracto bancario de la entidad emisora (NIT, fecha, monto, concepto)
- Anticipos en efectivo: se cruzan contra gastos legalizados con soportes (facturas, recibos)
- Para efectos de la DIAN: los documentos soporte deben ser electronicos o digitalizados conforme a normativa de facturacion electronica

---

## 6. Plazo de Legalizacion

El retorno del dinero no utilizado y la legalizacion de gastos no deberia exceder un mes desde la fecha de retorno del viaje. El sistema debe controlar este plazo y generar alertas cuando se acerque el vencimiento.

---

## 7. Reglas Implementadas en el Sistema

| Regla | Implementacion |
|-------|---------------|
| Clasificacion obligatoria | El formulario exige seleccionar Ocasional o Permanente con justificacion |
| Desglose obligatorio | El empleado debe discriminar el monto por cada categoria de gasto |
| Calculo automatico de incidencia salarial | El sistema determina si cada linea de gasto constituye salario segun la matriz tipo vs categoria |
| Alerta a GH por incidencia salarial | Cuando tipo = Permanente y categoria = hospedaje o alimentacion |
| Registro de criterios de determinacion | El sistema almacena datos para evaluar habitualidad, frecuencia y naturaleza del viaje |
| Trazabilidad de clasificacion | Cada clasificacion queda registrada en auditoria con fecha, usuario y justificacion |
| Control de plazo de legalizacion | Alerta automatica cuando se acerca el plazo de 30 dias para legalizar |

---

## 8. Referencias

- Codigo Sustantivo del Trabajo, Articulo 130
- Jurisprudencia de la Corte Suprema de Justicia, Sala de Casacion Laboral
- Concepto del Ministerio de Trabajo sobre clasificacion de viaticos
- Normativa de facturacion electronica DIAN