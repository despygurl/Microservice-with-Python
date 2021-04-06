from pymongo import MongoClient
from models.books import database as db
import csv


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

if __name__ == '__main__':
    db = db()
    add_book()
    db.nosql_db.close()