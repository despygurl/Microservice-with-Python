from pymongo import MongoClient

nosql_db = MongoClient(
    host='localhost', 
    port=27017)                         # Menghubungkan dengan server default localhost
# print(nosql_db.list_database_names())

db = nosql_db.bios                      # Membuat/memilih database
mongo_doc = db.customers                # Memilih collection/tabel

print(mongo_doc)                        # Mencetak status

nosql_db.close()                        # Menutup koneksi