from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMainWindow
import sys

class ReverseNameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Reverter Nome")
        self.setGeometry(200, 200, 400, 200)

        self.label_name = QLabel("Digite seu nome: ")
        self.input_name = QLineEdit()

        self.button_reverse = QPushButton("Reverter")
        self.result_label =QLabel("")
        self.button_reverse.clicked.connect(self.reverse_name)

        


        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button_reverse)
        layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def reverse_name(self):
        name = self.input_name.text()
        self.result_label.setText(f"Nome invertido: {name[::-1]}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReverseNameWindow()
    window.show()
    sys.exit(app.exec())
