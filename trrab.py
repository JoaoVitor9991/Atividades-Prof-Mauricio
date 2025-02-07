from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys 

class  Imagem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T")
        self.setGeometry(200, 200, 600, 600)

        self.layout = QVBoxLayout()

        
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap())
        self.image_label.setScaledContents(True)


        self.butao1 = QPushButton("Imagem 1", self)
        self.butao2 = QPushButton("Imagem 2", self)

        self.butao1.setFixedSize(200, 50)
        self.butao2.setFixedSize(200, 50)

        self.butao1.clicked.connect(lambda: self.change_image("imagem1.jpg"))
        self.butao2.clicked.connect(lambda: self.change_image("imagem2.jpg"))

        self.layout.addWidget(self.butao1)
        self.layout.addWidget(self.butao2)
        self.layout.addWidget(self.image_label)
        self.setLayout(self.layout)


    def change_image(self, image_path):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Erro")
        else:
            pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
       
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Imagem() 
    window.show()
    sys.exit(app.exec())