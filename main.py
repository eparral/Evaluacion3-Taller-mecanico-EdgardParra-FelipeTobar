"""
Sistema CRUD - Taller Mecánico
Evaluación Unidad Integradora N°3 - Bases de Datos No Estructuradas

Ejecutar con: python main.py
Requiere una instancia de MongoDB corriendo en localhost:27017
"""
from pymongo.errors import ServerSelectionTimeoutError

from db import obtener_coleccion
from seed import generar_datos_precarga
from crud import (
    crear_cliente,
    listar_clientes,
    buscar_por_comparacion,
    buscar_por_regex,
    buscar_por_rango_fechas,
    buscar_en_subdocumento,
    actualizar_campo_raiz,
    actualizar_subdocumento_o_array,
    eliminar_documento,
    reporte_agregacion,
)


def precargar_datos_si_esta_vacia(coleccion):
    """Inserta los documentos de ejemplo solo si la colección está vacía."""
    if coleccion.count_documents({}) == 0:
        datos = generar_datos_precarga()
        coleccion.insert_many(datos)
        print(f"Se precargaron {len(datos)} documentos de ejemplo en la colección.")


def mostrar_menu():
    print("\n" + "=" * 55)
    print("   SISTEMA DE GESTIÓN - TALLER MECÁNICO")
    print("=" * 55)
    print("1. Crear nuevo cliente")
    print("2. Listar todos los clientes")
    print("3. Buscar por comparación (año / costo)")
    print("4. Buscar con expresión regular")
    print("5. Buscar por rango de fechas")
    print("6. Buscar dentro de subdocumento o array")
    print("7. Actualizar campo del documento raíz")
    print("8. Actualizar subdocumento o array")
    print("9. Eliminar cliente")
    print("10. Reporte con pipeline de agregación")
    print("0. Salir")
    print("=" * 55)


def main():
    try:
        coleccion = obtener_coleccion()
    except ServerSelectionTimeoutError:
        print("ERROR: No se pudo conectar a MongoDB en localhost:27017.")
        print("Verifique que el servicio de MongoDB está activo e intente nuevamente.")
        return

    precargar_datos_si_esta_vacia(coleccion)

    acciones = {
        "1": crear_cliente,
        "2": listar_clientes,
        "3": buscar_por_comparacion,
        "4": buscar_por_regex,
        "5": buscar_por_rango_fechas,
        "6": buscar_en_subdocumento,
        "7": actualizar_campo_raiz,
        "8": actualizar_subdocumento_o_array,
        "9": eliminar_documento,
        "10": reporte_agregacion,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        accion = acciones.get(opcion)
        if accion:
            try:
                accion(coleccion)
            except Exception as error:
                print(f"Ocurrió un error al ejecutar la operación: {error}")
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
