from mysql.connector import connect

class database:
    def __init__(self):
        try:
            self.db = connect(
                host = 'localhost',
                database = 'perpustakaan',
                user = 'root',
                password = '4m4li409')
        except Exception as e:
            print(e)

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

    def insertUser(self, **params):
        try:
            column = ', '.join(list(params['values'].keys()))
            values = tuple(list(params['values'].values()))
            crud_query ='insert into customers({0}) values {1}'.format(column, values)
            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)

    def updateUserById(self):
        pass

    def deleteUserById(self):
        pass

    def dataCommit(self):
        self.db.commit()