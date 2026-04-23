# Reglas de Negocio: Validaciones de Solicitud

Este documento detalla las validaciones logicas que deben implementarse en Dataverse y Power Apps para garantizar la integridad de las solicitudes de viaticos.

## 1. Validaciones de Integridad Temporal

- **Cronologia**: La `Fecha de Inicio del Viaje` debe ser menor o igual a la `Fecha Fin del Viaje`.
- **Anticipacion**: Las solicitudes con requerimiento de anticipo deben crearse al menos 5 dias habiles antes del inicio del viaje (Regla deseable, sujeta a excepcion por jefe).

## 2. Validaciones de Gastos (Art. 130 CST)

- **Desglose Obligatorio**: No se puede enviar una solicitud (`crb_estado` = 'Enviada') si no tiene al menos un registro en `DETALLE_GASTOS`.
- **Topes de Monto**: El monto ingresado para cada categoria en `DETALLE_GASTOS` debe ser menor o igual al valor configurado en `crb_config_topes_monto` para el par (Tipo de Destino, Categoria).
- **Consistencia de Totales**: La suma de los montos en `DETALLE_GASTOS` debe coincidir con el `crb_monto_estimado` de la solicitud principal.

## 3. Validaciones de Anticipo

- **Existencia de Monto**: Si `crb_requiere_anticipo` es 'Si', el campo `crb_monto_anticipo` debe ser obligatorio y mayor a cero.
- **Tope de Anticipo**: El `crb_monto_anticipo` no puede exceder el 100% del `crb_monto_estimado`.

## 4. Validaciones de Documentacion

- **Soportes Obligatorios**:
    - Si el viaje es Internacional, el documento tipo 'Invitacion' o 'Resolucion' es obligatorio.
    - Si se solicita anticipo, el documento tipo 'Soporte Anticipo' es obligatorio.

## 5. Validaciones de Flujo

- **Unica solicitud activa**: Un usuario no puede tener mas de una solicitud en estado 'Enviada' o 'Aprobada_Jefe' simultaneamente para evitar traslapes de viajes (Regla de negocio para mitigar fraudes).
