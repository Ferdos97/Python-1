
from dbmanager import DbManager
dbm = DbManager()

products = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT",
            "price": "REAL",
            "stock": "INTEGER"
}

dbm.create_table('product', products)

data = {"name":"phone", "price": 1100, "stock": 10}
dbm.insert('product', data)

# ----------------------------------

data = {"price": 100}
where = {"id": 2}
dbm.update('product', data, where)

# ----------------------------------

data = {"stock": 15}
where = {"id": 3}
dbm.update('product', data, where)

# ---------------------------------

data = {"stock": 5, 'name': 'new phone'}
where = {"id": 2}
dbm.update('product', data, where)

# ---------------------------------

where = {'id': 2}
result = dbm.get_one('product', where)
print(list(result))

# ----------------------------------

where = {'id <': 4}
result = dbm.get_many('product', where)
for item in result:
    print(list(item))

# ----------------------------------

where = {'id <': 4}
result = dbm.delete('product', where)
print(result)

# -----------------------------------

where = {'id =': 5}
result = dbm.delete('product', where)
print(result)
