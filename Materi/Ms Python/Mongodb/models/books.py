from pymongo import MongoClient
from bson import ObjectId

class database:
    def __init__(self):
        try:
            self.nosql_db = MongoClient()
            self.db = self.nosql_db.perpustakaan
            self.mongo_col = self.db.books
            print("database connected")
        except Exception as e:
            print(e)

    def showBooks(self):
        result = self.mongo_col.find()
        return result  

    def showBooksById(self,id):
        query = {"_id": ObjectId(id)}
        result = self.mongo_col.find(query)
        return result

    def searchBookByName(self, key):
        query = {"nama": {"$regex":key, "$options":"i"}}
        result = self.mongo_col.find(query)
        return result

    def insertBook(self, document):
        self.mongo_col.insert_one(document)

    def updateBookById(self, data):
        self.mongo_col.update_one(*data)

    def deleteBookById(self,id):
        query = {"_id": ObjectId(id)}
        result = self.mongo_col.delete_one(query)
        return result

