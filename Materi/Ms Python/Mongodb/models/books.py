from pymongo import MongoClient

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
        pass

    def showBooksById(self):
        pass

    def searchBookByName(self):
        pass

    def insertBook(self, document):
        self.mongo_col.insert_one(document)

    def updateBookById(self):
        pass

    def deleteBookById(self):
        pass

