# Especificacion de Pantallas - Power Apps Viaticos (MVP)

Este documento detalla el diseño de la interfaz de usuario para el sistema de viáticos, siguiendo la identidad institucional del Banco (Azul Marino y Oro).

## 1. Identidad Visual (Branding)

| Elemento | Color / Estilo | Proposito |
|----------|---------------|-----------|
| **Azul Marino** | `#002D72` | Cabeceras, paneles laterales y botones primarios. |
| **Oro** | `#D4AF37` | Bordes de resaltado, iconos de estado y micro-animaciones. |
| **Gris Claro** | `#F4F4F4` | Fondo de la aplicación. |
| **Tipografia** | Segoe UI / Roboto | Lectura corporativa limpia. |

---

## 2. Pantalla 1: Dashboard del Empleado (`scr_EmployeeDashboard`)

Vista principal para que el solicitante gestione su historial.

- **Componentes**:
    - **Header**: Logo del Banco y nombre del usuario.
    - **Panel de Estadisticas**: 3 tarjetas con conteo de solicitudes (Borradores, En Proceso, Pagadas).
    - **Galeria Principal**: Lista de solicitudes con:
        - Icono de estado (Oro si es pendiente).
        - Destino y Fecha.
        - Monto Estimado.
    - **Boton Flotante (FAB)**: (+) Nueva Solicitud (Azul Marino con borde Oro).

---

## 3. Pantalla 2: Formulario de Solicitud (`scr_RequestForm`)

Interfaz para el ingreso de datos cumpliendo el Art. 130 CST.

- **Seccion 1: Datos Generales**:
    - Campos: Destino, Pais, Motivo, Fechas, Centro de Costo (Lookup searchable).
    - Toggle: ¿Requiere Anticipo? (Muestra/Oculta monto anticipo).
- **Seccion 2: Desglose de Gastos (Editable Grid)**:
    - Tabla embebida para agregar filas a `crb_detalle_gastos`.
    - Columnas: Categoria, Monto, Descripcion.
    - Validacion en tiempo real: Suma de desglose debe ser <= Monto Estimado.
- **Seccion 3: Documentación**:
    - Control de adjuntos para subir archivos PDF/JPG.

---

## 4. Pantalla 3: Tracking de Solicitud (`scr_RequestTracking`)

Visualización del progreso y auditoría.

- **Componentes**:
    - **Timeline Horizontal**: Diagrama visual que muestra los niveles de aprobación (Completado: Azul, Pendiente: Oro).
    - **Panel Lateral**: Detalles del flujo (Aprobador actual, tiempo en espera).
    - **Visor de Documentos**: Previsualización de los archivos cargados.

---

## 5. Pantalla 4: Consola de Aprobacion (`scr_ApprovalConsole`)

Vista exclusiva para Jefes y GH (Filtros por RBAC).

- **Filtros**: Por fecha, por solicitante, por estado.
- **Acciones Masivas**: Seleccionar varias y aprobar (con confirmacion).
- **Vista Detalle**: Al seleccionar una, abre un pop-up con el desglose legal y botones GRANDES de **Aprobar** (Verde) y **Rechazar** (Rojo).

---

## 6. Lógica de Navegación

- Al iniciar: Si el usuario es Admin, redirigir a un panel de configuración.
- Al enviar: Mostrar pantalla de éxito con confeti institucional (Oro) y botón para volver al Dashboard.
- Al rechazar: Abrir modal obligatorio para ingreso de comentario.
