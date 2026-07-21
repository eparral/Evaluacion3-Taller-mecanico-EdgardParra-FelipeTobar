import os

from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "taller_mecanico_db"
COLLECTION_NAME = "clientes"


def obtener_coleccion():
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    cliente.admin.command("ping")
    db = cliente[DB_NAME]
    coleccion = db[COLLECTION_NAME]
    return coleccion
