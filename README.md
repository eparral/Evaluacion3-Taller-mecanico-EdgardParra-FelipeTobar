# Sistema CRUD - Taller Mecánico

Evaluación Unidad Integradora N°3 — Bases de Datos No Estructuradas (INACAP).
Sistema de consola para gestionar clientes, vehículos y servicios de un taller mecánico, desarrollado con Python, PyMongo y MongoDB.

## Integrantes

- Nombre Apellido 1
- Nombre Apellido 2

> Reemplazar los nombres antes de publicar el repositorio.

## Requisitos

- Python 3.10 o superior
- MongoDB local activo en `localhost:27017`
- Git

## Instalación y ejecución

```bash
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DE_LA_CARPETA
python -m venv .venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Al iniciar por primera vez, el sistema usa `insert_many()` para precargar 8 documentos si la colección está vacía. Los documentos se almacenan en la colección `clientes` de la base `taller_mecanico_db`.

Opcionalmente, la conexión se puede cambiar con la variable de entorno `MONGO_URI`; si no se define, se usa MongoDB local.

## Modelo de datos

Cada cliente contiene:

- Campos raíz: `nombre_cliente`, `rut_cliente`, `telefono`, `email` y `fecha_registro` (`Date`).
- Subdocumento `vehiculo`: marca, modelo, año, patente y color.
- Array de subdocumentos `historial_servicios`: fecha, tipo, descripción, costo, mecánico y estado.

## Funcionalidades

1. Crear un cliente completo mediante `insert_one()`.
2. Listar todos los clientes.
3. Consultar año o costo usando `$gt`, `$lt`, `$gte`, `$lte`, `$ne` o `$in`, con proyección.
4. Buscar nombre o marca mediante `$regex`.
5. Buscar registros por rango de fechas.
6. Consultar un subdocumento o un array mediante notación punto y `$elemMatch`.
7. Actualizar teléfono o email con `$set`, mostrando antes y después.
8. Actualizar el vehículo o historial mediante `$set` y `$push`, mostrando antes y después.
9. Eliminar por RUT, mostrando el documento y solicitando confirmación.
10. Generar un reporte por mecánico con `$unwind`, `$match`, `$group` y `$sort`.

## Estructura

```text
.
|-- main.py
|-- db.py
|-- crud.py
|-- seed.py
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Guion recomendado para la demo

1. Mostrar el repositorio público, los integrantes y este README.
2. Confirmar MongoDB activo, clonar el repositorio en una carpeta nueva e instalar dependencias.
3. Ejecutar `python main.py` y mostrar la precarga de 8 documentos.
4. Ejecutar las opciones 2 a 6 para demostrar listado, comparación, regex, fechas y consultas anidadas.
5. Crear un cliente; anotar su RUT para luego actualizarlo y eliminarlo.
6. Ejecutar las dos clases de actualización y mostrar el antes/después.
7. Ejecutar el reporte de agregación y explicar brevemente sus cuatro etapas.
8. Eliminar el cliente de prueba confirmando la operación.

La entrega en el Ambiente de Aprendizaje es un archivo `.txt` que contenga la URL pública del repositorio y el nombre exacto de la rama utilizada, por ejemplo:

```text
URL: https://github.com/usuario/taller-mecanico-mongodb
Rama: main
```
