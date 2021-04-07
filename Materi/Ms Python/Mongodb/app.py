# Import library dan package yang dibutuhkan
from pymongo import MongoClient
from models.books import database as db
from bson import ObjectId
import csv

# Fungsi untuk tambah data
def add_book():
    data = open('bestsellers-with-categories.csv', encoding='utf-8')
    books = csv.reader(data, delimiter=',')
    next(books)     # Untuk melewati/skip baris pertama, sehingga baris pertama tidak akan dicetak

    for book in books:
        try:
            data = {
                'nama':book[0],
                'pengarang':book[1],
                'tahun terbit':book[5],
                'genre':book[6]
            }
            db.insertBook(data)
        except Exception as e:
            print('Kesalahan pada saat memasukkan data: {}'.format(e))
            break

# Fungsi untuk menampilkan data berdasarkan nama
def search_books(params):
    for book in db.searchBookByName(params):
        print(book)

# Fungsi untuk menampilkan seluruh data buku
def show_books():
    for data in db.showBooks():
        print(data)

# Fungsi untuk menampilkan data buku berdasarkan id
def search_books_id(params):
    for bk in db.showBooksById(params):
        print(bk)

# Fungsi untuk mengupdate data
def update_id():
    try:
        id_book = input("Masukkan id yang ingin diubah: ")
        nama = input("Masukkan nama terupdate: ")
        pengarang = input("Masukkan nama pengarang terupdate: ") 
        tahun_terbit = input("Masukkan tahun terbit terupdate: ")
        genre = input("Masukkan genre terupdate: ")

        print("\n====== Data Awal ======")
        show_awal = db.showBooksById(id_book)
        for buku in show_awal:
            print(buku,"\n")

        data = {"_id":ObjectId(id_book)},{
            "$set": {
            "nama":nama,
            "pengarang":pengarang,
            "tahun terbit":tahun_terbit,
            "genre":genre}}
        db.updateBookById(*data)

        print("\n====== Data Update ======")
        show_update = db.showBooksById(id_book)
        for buku in show_update:
            print(buku)

    except Exception as e:
        print('Kesalahan pada saat memasukkan data: {}'.format(e))

# Fungsi untuk menghapus data berdasarkan id
def delete_books_id(params):
    db.deleteBookById(params)
    print("Data sudah dihapus")


# Proses untuk memanggil fungsi yang dibutuhkan
if __name__ == '__main__':
    db = db()

    # add_book()
    # kata_kunci = input('Input kata kunci untuk pencarian judul buku: ')
    # search_books(kata_kunci)
    # show_books()
    # id_book = input('Input id buku untuk pencarian data buku: ')
    # kunci = input("Masukkan field yang ingin diubah (nama/pengarang/tahun terbit/genre): ")
    # search_books_id(id_book)
    # update_id()
    # delete_books_id(id_book)

    db.nosql_db.close()