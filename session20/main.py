
# sql --> crud
# create, read, update, delete
# mysql, postgress, sqlite
# python sqlite3

##----------------------------------

# 1 - connection
# 2 - cursor
# 3 - command
# 4 - execute command
# 5 - commit

##----------------------------------

## create: CREATE TABLE <tablename>(field1, filed2, filed3)

import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

command = """
    CREATE TABLE product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        stock INTEGER
)
"""
cur.execute(command)


command = "CREATE TABLE IF NOT EXIST user(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, user_name TEXT, password TEXT)"
cur.execute(command)


command = "CREATE TABLE orders(id, user_id, product_id)"
cur.execute(command)


cur.execute("""
    INSERT INTO user VALUES
        (1, 'ali', 'akbari', 'ali@gmail.com', '1234'),
        (2,'reza', 'akbari', 'reza@gmail.com', '9876')
""")

con.commit()

##or

command = '''
    INSERT INTO user VALUES
        (1, 'ali', 'akbari', 'ali@gmail.com', '1234'),
        (2,'reza', 'akbari', 'reza@gmail.com', '9876')
'''

cur.execute(command)
con.commit()
