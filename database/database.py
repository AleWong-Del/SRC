import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database/sistema_esportivo.db')
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=()):
        return self.cursor.execute(sql, params)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()