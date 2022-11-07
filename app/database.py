from os import getenv
from typing import Dict, Iterable, Iterator

from pymongo import MongoClient
from dotenv import load_dotenv
from certifi import where


class MongoDB:
    load_dotenv()
    client = MongoClient(getenv("MONGO_URL"), tlsCAFile=where())
    database = client["Prototype"]

    def __init__(self, collection_name: str):
        self.collection = self.database[collection_name]

    def create_one(self, record: Dict) -> bool:
        return self.collection.insert_one(record).acknowledged

    def read_one(self, query: Dict) -> Dict:
        return self.collection.find_one(query, {"_id": False})

    def create(self, records: Iterable[Dict]) -> bool:
        return self.collection.insert_many(records).acknowledged

    def read(self, query: Dict) -> Iterator[Dict]:
        return self.collection.find(query, {"_id": False})

    def update(self, query, update) -> bool:
        return self.collection.update(query, {"$set": update}).acknowledged

    def delete(self, query) -> bool:
        return self.collection.delete_many(query).acknowledged
