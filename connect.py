from pymongo import MongoClient
import pymongo.errors as errors
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener configuración
MONGODB_URI_ATLAS = os.getenv("MONGODB_URI_ATLAS")
DATABASE_NAME = os.getenv("MONGODB_Data")
# Crear cliente MongoDB
try:
    client = MongoClient(
        MONGODB_URI_ATLAS,
        tls=True,
        tlsAllowInvalidCertificates=True
    )

    # Conectar a la base de datos
    db = client[DATABASE_NAME]

    # Imprimir información de conexión
    print("Conexión exitosa a MongoDB Atlas")
    print("Base de datos:", DATABASE_NAME)
    print("Colecciones disponibles:", db.list_collection_names())

except errors.ConnectionFailure as e:
    print("No se pudo conectar al servidor", e)

except errors.ConfigurationError as e:
    print("Error de Autentificacion o permisos:", e)
    print("Error de Autentificacion o permisos:", e)
