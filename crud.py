"""
Operaciones CRUD y pipeline de agregación para el sistema
del Taller Mecánico.
"""
from datetime import datetime, timedelta


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def _pedir_fecha(mensaje):
    """Solicita una fecha en formato DD-MM-AAAA y la retorna como datetime."""
    while True:
        texto = input(mensaje).strip()
        try:
            return datetime.strptime(texto, "%d-%m-%Y")
        except ValueError:
            print("Formato inválido. Use DD-MM-AAAA, por ejemplo 15-03-2025.")


def _pedir_numero(mensaje, tipo=float):
    while True:
        texto = input(mensaje).strip()
        try:
            return tipo(texto)
        except ValueError:
            print("Debe ingresar un número válido.")


def _imprimir_documento(doc):
    print("-" * 60)
    print(f"ID: {doc.get('_id')}")
    print(f"Cliente: {doc.get('nombre_cliente')} | RUT: {doc.get('rut_cliente')}")
    print(f"Teléfono: {doc.get('telefono')} | Email: {doc.get('email')}")
    veh = doc.get("vehiculo", {})
    print(f"Vehículo: {veh.get('marca')} {veh.get('modelo')} ({veh.get('anio')}) "
          f"- Patente: {veh.get('patente')} - Color: {veh.get('color')}")
    print(f"Fecha de registro: {doc.get('fecha_registro')}")
    historial = doc.get("historial_servicios", [])
    if historial:
        print("Historial de servicios:")
        for i, serv in enumerate(historial, start=1):
            print(f"  {i}. [{serv.get('fecha_servicio')}] {serv.get('tipo_servicio')} "
                  f"- {serv.get('descripcion')} - ${serv.get('costo')} "
                  f"- Mecánico: {serv.get('mecanico_asignado')} - Estado: {serv.get('estado')}")
    print("-" * 60)


def _imprimir_lista(cursor):
    documentos = list(cursor)
    if not documentos:
        print("No se encontraron documentos.")
        return
    for doc in documentos:
        _imprimir_documento(doc)
    print(f"Total de documentos encontrados: {len(documentos)}")


# ---------------------------------------------------------------------------
# 1. CREATE
# ---------------------------------------------------------------------------

def crear_cliente(coleccion):
    print("\n--- Crear nuevo cliente ---")
    nombre = input("Nombre del cliente: ").strip()
    rut = input("RUT del cliente: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()

    print("\nDatos del vehículo:")
    marca = input("  Marca: ").strip()
    modelo = input("  Modelo: ").strip()
    anio = _pedir_numero("  Año: ", int)
    patente = input("  Patente: ").strip()
    color = input("  Color: ").strip()

    print("\nPrimer servicio a registrar en el historial:")
    fecha_servicio = _pedir_fecha("  Fecha del servicio (DD-MM-AAAA): ")
    tipo_servicio = input("  Tipo de servicio: ").strip()
    descripcion = input("  Descripción: ").strip()
    costo = _pedir_numero("  Costo: ")
    mecanico = input("  Mecánico asignado: ").strip()
    estado = input("  Estado (Completado/Pendiente): ").strip()

    documento = {
        "nombre_cliente": nombre,
        "rut_cliente": rut,
        "telefono": telefono,
        "email": email,
        "vehiculo": {
            "marca": marca,
            "modelo": modelo,
            "anio": anio,
            "patente": patente,
            "color": color
        },
        "historial_servicios": [
            {
                "fecha_servicio": fecha_servicio,
                "tipo_servicio": tipo_servicio,
                "descripcion": descripcion,
                "costo": costo,
                "mecanico_asignado": mecanico,
                "estado": estado
            }
        ],
        "fecha_registro": datetime.now()
    }

    resultado = coleccion.insert_one(documento)
    print(f"\nCliente creado correctamente. ID insertado: {resultado.inserted_id}")


# ---------------------------------------------------------------------------
# 2. LISTAR (Read básico)
# ---------------------------------------------------------------------------

def listar_clientes(coleccion):
    print("\n--- Listado completo de clientes ---")
    cursor = coleccion.find({})
    _imprimir_lista(cursor)


# ---------------------------------------------------------------------------
# 3. BUSCAR con operador de comparación (Read básico)
# ---------------------------------------------------------------------------

def buscar_por_comparacion(coleccion):
    print("\n--- Buscar con operador de comparación ---")
    print("1. Año del vehículo")
    print("2. Costo de un servicio (dentro del historial)")
    opcion = input("Seleccione el campo a comparar: ").strip()

    operadores = {
        "1": "$gt", "2": "$lt", "3": "$gte", "4": "$lte", "5": "$ne", "6": "$in"
    }
    print("Operadores disponibles: 1) $gt 2) $lt 3) $gte 4) $lte 5) $ne 6) $in")
    op_key = input("Seleccione el operador: ").strip()
    operador = operadores.get(op_key, "$gt")

    if opcion == "1":
        valor = int(_pedir_numero("Ingrese el año a comparar: ", int))
        if operador == "$in":
            valor = [valor, valor + 1]  # ejemplo simple de lista para $in
        filtro = {"vehiculo.anio": {operador: valor}}
        proyeccion = {"nombre_cliente": 1, "vehiculo": 1, "_id": 0}
        cursor = coleccion.find(filtro, proyeccion)
    else:
        valor = _pedir_numero("Ingrese el costo a comparar: ")
        if operador == "$in":
            valor = [valor]
        filtro = {"historial_servicios.costo": {operador: valor}}
        proyeccion = {"nombre_cliente": 1, "historial_servicios": 1, "_id": 0}
        cursor = coleccion.find(filtro, proyeccion)

    print(f"\nResultados con filtro: {filtro}")
    for doc in cursor:
        print(doc)


# ---------------------------------------------------------------------------
# 4. BUSCAR con expresión regular (Read avanzado)
# ---------------------------------------------------------------------------

def buscar_por_regex(coleccion):
    print("\n--- Buscar con expresión regular ---")
    print("1. Por nombre de cliente")
    print("2. Por marca de vehículo")
    opcion = input("Seleccione el campo: ").strip()
    texto = input("Ingrese el texto o patrón a buscar: ").strip()

    if opcion == "2":
        campo = "vehiculo.marca"
    else:
        campo = "nombre_cliente"

    filtro = {campo: {"$regex": texto, "$options": "i"}}
    cursor = coleccion.find(filtro)
    _imprimir_lista(cursor)


# ---------------------------------------------------------------------------
# 5. BUSCAR por rango de fechas (Read avanzado)
# ---------------------------------------------------------------------------

def buscar_por_rango_fechas(coleccion):
    print("\n--- Buscar por rango de fechas (fecha de registro) ---")
    fecha_inicio = _pedir_fecha("Fecha de inicio (DD-MM-AAAA): ")
    fecha_fin = _pedir_fecha("Fecha de fin (DD-MM-AAAA): ")
    if fecha_fin < fecha_inicio:
        print("La fecha final no puede ser anterior a la fecha inicial.")
        return

    # El límite exclusivo del día siguiente incluye todas las horas del día final.
    filtro = {
        "fecha_registro": {
            "$gte": fecha_inicio,
            "$lt": fecha_fin + timedelta(days=1),
        }
    }
    cursor = coleccion.find(filtro)
    _imprimir_lista(cursor)


# ---------------------------------------------------------------------------
# 6. BUSCAR dentro de subdocumento o array (Read avanzado)
# ---------------------------------------------------------------------------

def buscar_en_subdocumento(coleccion):
    print("\n--- Buscar dentro de subdocumento o array ---")
    print("1. Buscar por marca exacta del vehículo (subdocumento)")
    print("2. Buscar clientes con un tipo de servicio específico (array de subdocumentos)")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        marca = input("Ingrese la marca exacta: ").strip()
        filtro = {"vehiculo.marca": marca}
    else:
        tipo_servicio = input("Ingrese el tipo de servicio (ej: Cambio de aceite): ").strip()
        filtro = {"historial_servicios": {"$elemMatch": {"tipo_servicio": tipo_servicio}}}

    cursor = coleccion.find(filtro)
    _imprimir_lista(cursor)


# ---------------------------------------------------------------------------
# 7. ACTUALIZAR campo del documento raíz (Update)
# ---------------------------------------------------------------------------

def actualizar_campo_raiz(coleccion):
    print("\n--- Actualizar campo del documento raíz ---")
    rut = input("Ingrese el RUT del cliente a actualizar: ").strip()
    doc = coleccion.find_one({"rut_cliente": rut})
    if not doc:
        print("No se encontró un cliente con ese RUT.")
        return

    print("Documento antes de la actualización:")
    _imprimir_documento(doc)

    print("Campos editables: telefono, email")
    campo = input("¿Qué campo desea actualizar?: ").strip()
    if campo not in ("telefono", "email"):
        print("Campo no válido.")
        return
    nuevo_valor = input(f"Nuevo valor para {campo}: ").strip()

    coleccion.update_one({"rut_cliente": rut}, {"$set": {campo: nuevo_valor}})
    doc_actualizado = coleccion.find_one({"rut_cliente": rut})
    print("\nDocumento después de la actualización:")
    _imprimir_documento(doc_actualizado)


# ---------------------------------------------------------------------------
# 8. ACTUALIZAR dentro de subdocumento o array (Update)
# ---------------------------------------------------------------------------

def actualizar_subdocumento_o_array(coleccion):
    print("\n--- Actualizar dentro de subdocumento o array ---")
    rut = input("Ingrese el RUT del cliente a actualizar: ").strip()
    doc = coleccion.find_one({"rut_cliente": rut})
    if not doc:
        print("No se encontró un cliente con ese RUT.")
        return

    print("1. Actualizar color del vehículo (subdocumento)")
    print("2. Agregar un nuevo servicio al historial ($push)")
    print("3. Actualizar el estado de un servicio existente (array, por tipo de servicio)")
    opcion = input("Seleccione una opción: ").strip()

    print("Documento antes de la actualización:")
    _imprimir_documento(doc)

    if opcion == "1":
        nuevo_color = input("Nuevo color del vehículo: ").strip()
        coleccion.update_one({"rut_cliente": rut}, {"$set": {"vehiculo.color": nuevo_color}})

    elif opcion == "2":
        fecha_servicio = _pedir_fecha("Fecha del nuevo servicio (DD-MM-AAAA): ")
        tipo_servicio = input("Tipo de servicio: ").strip()
        descripcion = input("Descripción: ").strip()
        costo = _pedir_numero("Costo: ")
        mecanico = input("Mecánico asignado: ").strip()
        estado = input("Estado (Completado/Pendiente): ").strip()

        nuevo_servicio = {
            "fecha_servicio": fecha_servicio,
            "tipo_servicio": tipo_servicio,
            "descripcion": descripcion,
            "costo": costo,
            "mecanico_asignado": mecanico,
            "estado": estado
        }
        coleccion.update_one(
            {"rut_cliente": rut},
            {"$push": {"historial_servicios": nuevo_servicio}}
        )

    elif opcion == "3":
        tipo_servicio = input("Tipo de servicio a actualizar (ej: Cambio de aceite): ").strip()
        nuevo_estado = input("Nuevo estado (Completado/Pendiente): ").strip()
        coleccion.update_one(
            {"rut_cliente": rut, "historial_servicios.tipo_servicio": tipo_servicio},
            {"$set": {"historial_servicios.$.estado": nuevo_estado}}
        )
    else:
        print("Opción no válida.")
        return

    doc_actualizado = coleccion.find_one({"rut_cliente": rut})
    print("\nDocumento después de la actualización:")
    _imprimir_documento(doc_actualizado)


# ---------------------------------------------------------------------------
# 9. ELIMINAR con condición específica (Delete)
# ---------------------------------------------------------------------------

def eliminar_documento(coleccion):
    print("\n--- Eliminar cliente ---")
    rut = input("Ingrese el RUT del cliente a eliminar: ").strip()
    doc = coleccion.find_one({"rut_cliente": rut})
    if not doc:
        print("No se encontró un cliente con ese RUT.")
        return

    print("Documento que será eliminado:")
    _imprimir_documento(doc)
    confirmacion = input("¿Confirma la eliminación? (S/N): ").strip().upper()
    if confirmacion == "S":
        resultado = coleccion.delete_one({"rut_cliente": rut})
        print(f"Documentos eliminados: {resultado.deleted_count}")
    else:
        print("Operación cancelada.")


# ---------------------------------------------------------------------------
# 10. REPORTE con pipeline de agregación
# ---------------------------------------------------------------------------

def reporte_agregacion(coleccion):
    print("\n--- Reporte: total facturado y cantidad de servicios por mecánico ---")
    pipeline = [
        {"$unwind": "$historial_servicios"},
        {"$match": {"historial_servicios.estado": "Completado"}},
        {
            "$group": {
                "_id": "$historial_servicios.mecanico_asignado",
                "total_facturado": {"$sum": "$historial_servicios.costo"},
                "cantidad_servicios": {"$sum": 1}
            }
        },
        {"$sort": {"total_facturado": -1}}
    ]

    resultados = list(coleccion.aggregate(pipeline))
    if not resultados:
        print("No hay resultados para mostrar.")
        return

    print(f"{'Mecánico':<20}{'Total facturado':<20}{'N° servicios':<15}")
    print("-" * 55)
    for r in resultados:
        print(f"{r['_id']:<20}${r['total_facturado']:<19}{r['cantidad_servicios']:<15}")
