from os import getenv
from typing import Dict

from pymongo import MongoClient
from dotenv import load_dotenv
from certifi import where


class MongoDB:
    load_dotenv()
    client = MongoClient(getenv("MONGO_URL"), tlsCAFile=where())
    database = client["Prototype"]

    def __init__(self, collection_name: str):
        self.collection = self.database[collection_name]

    def create(self, record: Dict) -> bool:
        return self.collection.insert_one(record).acknowledged

    def read(self, query: Dict) -> Dict:
        return self.collection.find_one(query, {"_id": False})

    def update(self, query, update) -> bool:
        return self.collection.update_one(query, {"$set": update}).acknowledged
