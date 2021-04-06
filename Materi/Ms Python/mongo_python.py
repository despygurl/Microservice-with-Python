from pymongo import MongoClient

nosql_db = MongoClient(
    host='localhost', 
    port= 27017)                         # Menghubungkan dengan server default localhost
# print(nosql_db.list_database_names())  # Menampilkan list database

db = nosql_db.rentalfilm                      # Membuat/memilih database
mongo_doc = db.bios                # Memilih collection/tabel

# print(mongo_doc)                      # Mencetak status



# Mencari/Menampilkan seluruh data
print("==== Menampilkan Seluruh Data di Tabel Bios ====")
result = mongo_doc.find()
for data in result:
    print(data)

# Menampilkan data tertentu dengan query
print("\n==== Menampilkan Data yang Telah Diquery ====")
query = {
    'awards.year' : {'$gt':1990, '$lt':2000},
    'contribs' : 'OOP'}

res = mongo_doc.find(query)

for dt in res:
    print(dt)




nosql_db.close()                        # Menutup koneksi