from PyQt6 import QtWidgets, uic
from dao.aluno_repository import AlunoRepository

class AdminHomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pages/admin_home_UI.ui', self)
        
        self.aluno_repo = AlunoRepository()
        self.atualizar_lista()

    def atualizar_lista(self):
        alunos = self.aluno_repo.listar_todos()
        # Exemplo: preencher uma QListWidget ou QTableWidget chamada 'lista_alunos'
        self.lista_alunos.clear()
        for aluno in alunos:
            self.lista_alunos.addItem(f"{aluno.nome} - CPF: {aluno.cpf}")