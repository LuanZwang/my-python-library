from pymongo import MongoClient

class BaseRepository:
    def __init__(self, connectionString, database, collectionName) -> None:
        self.db = MongoClient(connectionString)[database][collectionName]

