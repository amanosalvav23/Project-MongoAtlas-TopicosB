from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI_ATLAS = os.getenv("MongoDB_URI_ATLAS")
DATABASE_NAME = os.getenv("MongoDB_Data")

try:
    client = MongoClient(MONGODB_URI_ATLAS)
    print("Conexion Exitosa a MongoDB Atlas")
    db = client[DATABASE_NAME]
    colecciones = db.list_collection_names()
    print("Conectando Atlas, Base de datos", (DATABASE_NAME))
    print("Colecciones disponibles:", colecciones)

except errors.ConnectionFailure as e:
    print("No se pudo conectar al servidor", e)

except errors.ConfigurationError as e:
    print("Error de Autentificacion o permisos:", e)
