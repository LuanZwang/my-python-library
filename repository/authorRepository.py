# from pymongo import MongoClient
from bson import ObjectId
from .base.baseRepository import BaseRepository

class AuthorRepository(BaseRepository):
    def __init__(self, connectionString, database, collection) -> None:
        super().__init__(connectionString, database, collection)

    def insert_one(self, data):
        self.db.insert_one(data) #= MongoClient("mongodb://admin:admin@localhost:27017")["flask_api"]["something_else"]
        # db.insert_one({ "name":"Luanzito" })

    def find(self, data_id):
        if id is None:
            return self.db.aggregate([
                {
                    "$addFields": { "id": { "$toString": "$_id" } }
                },
                {
                    "$unset":{ "_id" }
                }
            ])

        return self.db.aggregate([
                {
                    "$match": { '_id': ObjectId(data_id)}
                },
                {
                    "$addFields": { "id": { "$toString": "$_id" } }
                },
                {
                    "$unset": [ "_id" ]
                }
            ])
