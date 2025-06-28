from pymongo import MongoClient

# URI de conexión (puedes usar directamente o cargar desde un .env)
MONGO_URI = "mongodb+srv://cvenegasm7:AQpmqBtfnEdeNimd@cluster0.4mrk1sn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Nombre de base de datos y colección
db_name = "crypto"
collection_name = "listings"

try:
    # Crear cliente de conexión
    client = MongoClient(MONGO_URI)

    # Probar conexión
    db = client[db_name]
    collection = db[collection_name]

    # Leer un documento
    doc = collection.find_one()
    if doc:
        print("✅ Conexión exitosa. Ejemplo de documento:")
        print(doc)
    else:
        print("✅ Conectado, pero no se encontraron documentos.")
except Exception as e:
    print("❌ Error al conectar a MongoDB:", e)
