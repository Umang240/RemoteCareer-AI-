from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI") or os.getenv("MONGODB_URL")
if not MONGO_URI:
    raise EnvironmentError(
        "MONGO_URI or MONGODB_URL must be set in the environment."
    )

client = MongoClient(MONGO_URI)

db = client[os.getenv("DATABASE_NAME", "careergpt")]

profiles_collection = db["profiles"]

print("MongoDB Connected")