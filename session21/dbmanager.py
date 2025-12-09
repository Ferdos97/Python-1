import sqlite3

class DbManager:
    def __init__(self, db_name="session21/database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row     # return rows as dict-like objects
        self.cur = self.conn.cursor()

    # -----------------------
    # CREATE TABLE
    # -----------------------
    def create_table(self, table_name, columns: dict): #*args
        """
        columns = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT",
            "price": "REAL",
            "stock": "INTEGER"
        }
        """

        cols = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols});"
        self.cur.execute(query)
        self.conn.commit()

    # -----------------------
    # INSERT RECORD
    # -----------------------
    def insert(self, table_name, data: dict):
        """
        data = {"name": "Laptop", "price": 1200, "stock": 10}
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cur.execute(query, list(data.values()))
        self.conn.commit()
        return self.cur.lastrowid  # return new id

    # -----------------------
    # UPDATE RECORD
    # -----------------------
    def update(self, table_name, data: dict, where: dict):
        """
        data = {"price": 999}
        where = {"id": 1}
        """
        set_clause = ", ".join([f"{key}=?" for key in data])
        where_clause = " AND ".join([f"{key}=?" for key in where])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        values = list(data.values()) + list(where.values())
        self.cur.execute(query, values)
        self.conn.commit()
        return self.cur.rowcount  # number of rows updated

    # -----------------------
    # GET ONE
    # -----------------------
    def get_one(self, table_name, where: dict):
        where_clause = " AND ".join([f"{key}=?" for key in where])
        query = f"SELECT * FROM {table_name} WHERE {where_clause} LIMIT 1"
        self.cur.execute(query, list(where.values()))
        return self.cur.fetchone()

    # -----------------------
    # GET MANY
    # -----------------------
    def get_many(self, table_name, where: dict = None):
        if where:
            where_clause = " AND ".join([f"{key}=?" for key in where])
            query = f"SELECT * FROM {table_name} WHERE {where_clause}"
            self.cur.execute(query, list(where.values()))
        else:
            query = f"SELECT * FROM {table_name}"
            self.cur.execute(query)
        return self.cur.fetchall()

    # -----------------------
    # DELETE
    # -----------------------
    def delete(self, table_name, where: dict):
        where_clause = " AND ".join([f"{key}=?" for key in where])
        query = f"DELETE FROM {table_name} WHERE {where_clause}"
        self.cur.execute(query, list(where.values()))
        self.conn.commit()
        return self.cur.rowcount

    # -----------------------
    # CLOSE DB
    # -----------------------
    def close(self):
        self.conn.close()