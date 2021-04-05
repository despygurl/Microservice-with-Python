from mysql.connector import connect

db = connect(
    host = 'localhost',
    user = 'root',
    passwd = '4m4li409',
    database = 'classicmodels'
)

# print(db)


# Melihat isi/data dari tabel
cursor = db.cursor()
query = 'select * from employees'

cursor.execute(query)
data = cursor.fetchall()
for row in data:
    print(row)
