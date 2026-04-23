# Logica de Calculo: Incidencia Salarial (Art. 130 CST)

Este documento describe la logica automatizada para determinar que parte de los viaticos constituye salario, garantizando el cumplimiento del **Articulo 130 del Codigo Sustantivo del Trabajo (CST)** de Colombia.

## 1. Fundamento Legal

El Art. 130 del CST establece:
- **Viaticos Accidentales**: Son aquellos que solo se dan con motivo de un requerimiento extraordinario. **No constituyen salario** en ningun caso.
- **Viaticos Permanentes**: Son aquellos que se dan por el desempeño habitual de las funciones.
    - La parte destinada a **Hospedaje y Alimentacion** constituye salario.
    - La parte destinada a **Transporte y Gastos de Representacion** no constituye salario.

## 2. Implementacion en el Sistema

### 2.1 Definicion de Viatico Permanente
Para efectos del sistema, una solicitud se marca como `crb_tipo_viatico` = 'Permanente' si el empleado cumple mas de 15 dias de viaje en un mes calendario o si su contrato define la movilidad como condicion habitual.

### 2.2 Algoritmo de Marcacion
En la entidad `DETALLE_GASTOS`, el campo calculado `crb_constituye_salario` sigue la siguiente formula logic:

```excel
IF(
    AND(
        Solicitud.crb_tipo_viatico == 'Permanente',
        OR(
            crb_categoria_gasto == 'Hospedaje',
            crb_categoria_gasto == 'Alimentacion'
        )
    ),
    true,
    false
)
```

### 2.3 Calculo del Valor Salarial
El valor total que se reportara a la nomina (SAP HR) como base salarial para la solicitud es:

`Monto_Salarial = SUMATORIA(crb_monto WHERE crb_constituye_salario == true)`

## 3. Reporte a SAP
Este monto debe enviarse a SAP en un concepto de nomina especifico (Wage Type) durante el flujo de pago, para que se apliquen las retenciones de ley y aportes a seguridad social correspondientes.
