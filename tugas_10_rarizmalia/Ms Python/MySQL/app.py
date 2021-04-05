# Import customers.py
from models.customers import database

# Isi database awal yang akan di-insert
data = {
    'params':[
        {
            'values':{
                'username':'userpertama',
                'namadepan':'rudi',
                'namabelakang':'roundhouse',
                'email':'rudi.roundhouse@gmail.com'
            }
        },
        {
            'values':{
                'username':'userkedua',
                'namadepan':'shiroe',
                'namabelakang':'ishigami',
                'email':'shiroe.ishigami@gmail.com'
            }
        },
        {
            'values':{
                'username':'userketiga',
                'namadepan':'akatsuki',
                'namabelakang':'horizon',
                'email':'akatsuki.horizon@gmail.com'
            }
        }
    ]
}


# Fungsi untuk memanggil query insert data dan mengaplikasikannya pada mysql
def tambahData(data):
    for param in data['params']:
        mysqldb.insertUser(**param)
    mysqldb.dataCommit()
    print('data berhasil ditambahkan')


# Fungsi untuk memanggil query show seluruh data dan mengaplikasikannya pada mysql
def showAll():
    mysqldb.showUsers()
    mysqldb.dataCommit()

# Fungsi untuk memanggil query show data by id dan mengaplikasikannya pada mysql
def shows_id():
    mysqldb.showUserById()
    mysqldb.dataCommit()


if __name__ == '__main__':
    mysqldb = database()
    if mysqldb.db.is_connected():
        print('Connected to MySQL database')
    
    # tambahData(data)
    # showAll()
    shows_id()

    if mysqldb.db is not None and mysqldb.db.is_connected():
        mysqldb.db.close()