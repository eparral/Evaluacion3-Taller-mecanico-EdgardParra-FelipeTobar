"""
Módulo de conexión a MongoDB.
Conexión local por defecto en el puerto 27017.
"""
import os

from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "taller_mecanico_db"
COLLECTION_NAME = "clientes"


def obtener_coleccion():
    """
    Establece la conexión con MongoDB local y retorna la colección 'clientes'.
    """
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Verifica que el servidor está disponible (lanza excepción si no responde)
    cliente.admin.command("ping")
    db = cliente[DB_NAME]
    coleccion = db[COLLECTION_NAME]
    return coleccion
