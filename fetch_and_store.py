import json
import os
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# === CONFIGURACIÓN ===
MONGO_URI = os.getenv("MONGO_URI")
COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY")
DB_NAME = "crypto"
COLLECTION_NAME = "listings"

# === API DE COINMARKETCAP ===
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': os.getenv("COINMARKETCAP_API_KEY"),
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    data = response.json()
    print(" Datos obtenidos de CoinMarketCap")

    # === CONEXIÓN A MONGO ===
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Agregar timestamp
    for item in data["data"]:
        item["fetched_at"] = datetime.utcnow()

    # Insertar en MongoDB
    result = collection.insert_many(data["data"])
    print(f" {len(result.inserted_ids)} registros insertados en MongoDB")

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print("❌ Error de conexión:", e)
except Exception as e:
    print("❌ Error:", e)
