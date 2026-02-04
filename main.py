import sys
from PyQt6 import QtWidgets, uic
from dao.servidor_repository import ServidorRepository

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pages/login_UI.ui', self) # Caminho organizado
        self.repo = ServidorRepository()
        self.btn_entrar.clicked.connect(self.logar)

    def logar(self):
        user = self.repo.buscar_login(self.input_email.text(), self.input_senha.text())
        if user:
            QtWidgets.QMessageBox.information(self, "Sucesso", f"Bem-vindo {user.nome}")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Dados inválidos!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())