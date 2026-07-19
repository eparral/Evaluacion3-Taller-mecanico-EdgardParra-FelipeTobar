# Taller mecánico con MongoDB

Este proyecto fue realizado para la **Evaluación Integradora N°3 de Bases de Datos No Estructuradas**. Elegimos desarrollar un sistema para un taller mecánico porque nos permite trabajar de manera clara con clientes, vehículos y distintos servicios realizados.

El programa funciona mediante un menú en consola. Desde ahí se pueden registrar clientes, hacer búsquedas, modificar datos, eliminar registros y generar un reporte. Para desarrollarlo usamos **Python**, **PyMongo** y **MongoDB**.

## Integrantes

- Edgard Parra
- Felipe Tobar

## ¿Qué permite hacer el programa?

El menú incluye las siguientes opciones:

1. Registrar un cliente junto con su vehículo y su primer servicio.
2. Mostrar todos los clientes guardados.
3. Buscar vehículos por año o servicios por costo usando operadores de comparación.
4. Buscar clientes o marcas aunque se escriba solo una parte del texto.
5. Buscar clientes registrados entre dos fechas.
6. Buscar información dentro del vehículo o del historial de servicios.
7. Modificar el teléfono o correo de un cliente.
8. Cambiar el color del vehículo, agregar un servicio o actualizar su estado.
9. Eliminar un cliente por su RUT, solicitando confirmación antes de borrarlo.
10. Mostrar cuánto ha facturado cada mecánico y cuántos servicios ha completado.

Cuando el programa se ejecuta por primera vez, se cargan automáticamente **8 clientes de ejemplo** si la colección está vacía. Esto permite probar todas las opciones sin tener que ingresar los datos uno por uno.

## ¿Cómo guardamos la información?

Usamos la base de datos `taller_mecanico_db` y la colección `clientes`. Cada documento representa a un cliente y contiene:

- Sus datos principales: nombre, RUT, teléfono y correo.
- Un subdocumento llamado `vehiculo`, con la marca, modelo, año, patente y color.
- Un array llamado `historial_servicios`, donde se guardan los trabajos realizados al vehículo.
- Una fecha de registro almacenada como tipo `Date` de MongoDB.

Un documento tiene una estructura similar a esta:

```javascript
{
  nombre_cliente: "Juan Pérez",
  rut_cliente: "12345678-9",
  telefono: "+56912345678",
  email: "juan.perez@mail.com",
  vehiculo: {
    marca: "Toyota",
    modelo: "Yaris",
    anio: 2019,
    patente: "ABCD12",
    color: "Rojo"
  },
  historial_servicios: [
    {
      tipo_servicio: "Cambio de aceite",
      costo: 35000,
      mecanico_asignado: "Carlos Soto",
      estado: "Completado"
    }
  ],
  fecha_registro: Date
}
```

## Requisitos para ejecutarlo

- Python 3.10 o superior.
- MongoDB ejecutándose localmente en `localhost:27017`.
- Git para clonar el repositorio.

## Instalación

Primero se debe clonar el repositorio y entrar a la carpeta:

```powershell
git clone https://github.com/eparral/Evaluacion3-Taller-mecanico-EdgardParra-FelipeTobar.git
cd Evaluacion3-Taller-mecanico-EdgardParra-FelipeTobar
```

Luego creamos un entorno virtual e instalamos PyMongo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Finalmente ejecutamos el sistema:

```powershell
python main.py
```

Si MongoDB no está iniciado, el programa mostrará un mensaje indicando que no se pudo realizar la conexión.

## Consultas de MongoDB utilizadas

Durante el desarrollo ocupamos distintos recursos de MongoDB vistos en clases:

- `insert_one()` e `insert_many()` para crear documentos.
- `$gt`, `$lt`, `$gte`, `$lte`, `$ne` y `$in` para comparar datos.
- `$regex` para realizar búsquedas de texto.
- `$elemMatch` y notación punto para consultar datos anidados.
- `$set` y `$push` para modificar documentos.
- `delete_one()` para eliminar mediante una condición.
- `$unwind`, `$match`, `$group` y `$sort` para generar el reporte por mecánico.

## Archivos del proyecto

```text
.
|-- main.py          Menú principal
|-- db.py            Conexión con MongoDB
|-- crud.py          Operaciones CRUD y reporte
|-- seed.py          Ocho documentos de ejemplo
|-- requirements.txt Dependencias del proyecto
|-- ENTREGA.txt      URL y rama para la entrega
`-- README.md        Explicación del proyecto
```

## Orden que usaremos en la demostración

Para la presentación pensamos seguir este orden:

1. Clonar el repositorio e instalar las dependencias.
2. Iniciar MongoDB y ejecutar `python main.py`.
3. Mostrar los 8 documentos cargados inicialmente.
4. Probar las búsquedas por comparación, texto, fechas y datos anidados.
5. Crear un cliente de prueba y anotar su RUT.
6. Modificar sus datos para mostrar el documento antes y después.
7. Ejecutar el reporte de servicios completados por mecánico.
8. Eliminar el cliente de prueba usando su RUT y confirmar la operación.

## Datos de entrega

```text
URL: https://github.com/eparral/Evaluacion3-Taller-mecanico-EdgardParra-FelipeTobar
Rama: main
```
