from database.database import Database
from datetime import datetime

def reset_total():
    db = Database()
    
    # Criar tabela caso não exista (Perfeito para GitHub)
    db.execute("""
        CREATE TABLE IF NOT EXISTS Servidor (
            id_servidor INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT, email TEXT UNIQUE, senha TEXT, 
            cargo TEXT, data_cadastro TEXT
        )
    """)

    db.execute("DELETE FROM Servidor") # Limpa tudo
    
    sql = "INSERT INTO Servidor (nome, email, senha, cargo, data_cadastro) VALUES (?, ?, ?, ?, ?)"
    valores = ('Admin Geral', 'admin@ifsport.edu.br', '123', 'Coordenador', datetime.now().strftime("%d/%m/%Y"))
    
    db.execute(sql, valores)
    db.commit()
    db.close()
    print("✅ Banco resetado! Login: admin@ifsport.edu.br | Senha: 123")

if __name__ == "__main__":
    reset_total()