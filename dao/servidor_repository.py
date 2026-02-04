from database.database import Database
from models.servidor import Servidor

class ServidorRepository:
    def __init__(self):
        self.db = Database()

    def buscar_login(self, email, senha):
        sql = "SELECT * FROM Servidor WHERE email = ? AND senha = ?"
        cursor = self.db.execute(sql, (email, senha))
        dados = cursor.fetchone()
        if dados:
            return Servidor(*dados)
        return None