from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mi aplicación de encriptación")

        self.encrypt_button = QPushButton("Encriptar")
        self.encrypt_button.clicked.connect(self.encrypt_file)

        self.decrypt_button = QPushButton("Desencriptar")
        self.decrypt_button.clicked.connect(self.decrypt_file)

        layout = QVBoxLayout()
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def encrypt_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            # Aquí podrías llamar a la función de encriptación con el archivo seleccionado

    def decrypt_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            # Aquí podrías llamar a la función de desencriptación con el archivo seleccionado
