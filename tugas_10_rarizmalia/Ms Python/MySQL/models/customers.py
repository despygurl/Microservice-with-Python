# Import MySQL Connector
from mysql.connector import connect

# Buat kelas untuk menampung operasi dan/atau manajemen database
class database:
    # Fungsi init untuk menampung inisiasi MySQL dan database
    def __init__(self):
        try:
            self.db = connect(
                host = 'localhost',
                database = 'perpustakaan',
                user = 'root',
                password = 'xxxx')
        except Exception as e:
            print(e)

    # Fungsi yang berisi query untuk menampilkan seluruh data pada tabel customers
    def showUsers(self):
        try:
            show_query ='select * from customers'
            cursor = self.db.cursor()
            cursor.execute(show_query)
            data = cursor.fetchall()
            for row in data:
                print(row)
        except Exception as e:
            print(e)

    # Fungsi yang berisi query untuk menampilkan data customer yang dipanggil by id
    def showUserById(self):
        try:
            id = int(input("Masukkan id customer: "))
            showid_query ='select * from customers where USERID = {0}'.format(id)
            cursor = self.db.cursor()
            cursor.execute(showid_query)
            dt = cursor.fetchall()
            for row in dt:
                print(row)
        except Exception as e:
            print(e)

    # Fungsi yang berisi query untuk menambah/insert data pada tabel customers
    def insertUser(self, **params):
        try:
            column = ', '.join(list(params['values'].keys()))
            values = tuple(list(params['values'].values()))
            crud_query ='insert into customers({0}) values {1}'.format(column, values)
            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)

    # Fungsi yang berisi query untuk mengubah/update data pada tabel customers by id
    def updateUserById(self):
        pass

    # Fungsi yang berisi query untuk menghapus data pada tabel customers by id
    def deleteUserById(self):
        pass

    # Fungsi yang berisi query untuk melakukan commit agar query yang diminta di atas dapat dijalankan
    def dataCommit(self):
        self.db.commit()