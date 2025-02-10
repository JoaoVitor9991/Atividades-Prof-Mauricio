import sys
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Cadastro")

        self.label_cpf = QLabel("CPF:")
        self.input_cpf = QLineEdit()
        self.input_cpf.setPlaceholderText("Digite seu CPF")

        self.label_name = QLabel("Nome Completo:")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Digite seu nome")

        self.label_phone = QLabel("Telefone:")
        self.input_phone = QLineEdit()
        self.input_phone.setPlaceholderText("Digite seu telefone")

        self.button_submit = QPushButton("Finalizar Cadastro")
        self.button_submit.clicked.connect(self.submit_data)

        layout = QVBoxLayout()
        layout.addWidget(self.label_cpf)
        layout.addWidget(self.input_cpf)
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.label_phone)
        layout.addWidget(self.input_phone)
        layout.addWidget(self.button_submit)

        self.setLayout(layout)

    def submit_data(self):
        cpf = self.input_cpf.text()
        name = self.input_name.text()
        phone = self.input_phone.text()
        print(f"Cadastro realizado: CPF={cpf}, Nome={name}, Telefone={phone}")

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")

        self.label_username = QLabel("Usuário:")
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Digite seu nome de usuário")

        self.label_password = QLabel("Senha:")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Digite sua senha")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton("Entrar")
        self.button_login.clicked.connect(self.check_login)

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def check_login(self):
        correct_username = "123"
        correct_password = ""

        username = self.input_username.text()
        password = self.input_password.text()

        if username == correct_username and password == correct_password:
            print("Login bem-sucedido! Abrindo tela de cadastro...")
            self.open_register()
        else:
            print("Usuário ou senha incorretos.")

    def open_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
