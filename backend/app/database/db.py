from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI") or os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "careergpt")

if not MONGO_URI:
    raise EnvironmentError(
        "MONGO_URI or MONGODB_URL must be set in the environment."
    )

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
users_collection = db["users"]
profiles_collection = db["profiles"]