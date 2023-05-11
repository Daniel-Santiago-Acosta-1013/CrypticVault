from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from app.encryption.aes import encrypt, decrypt
from app.file_handlers.text_file_handler import read_file, write_file

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
            data = read_file(fileName)
            key = "132we1d635we65dw65edw"
            encrypted_data = encrypt(key, data)
            write_file(fileName, encrypted_data)

    def decrypt_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            data = read_file(fileName)
            key = "132we1d635we65dw65edw"
            decrypted_data = decrypt(key, data)
            write_file(fileName, decrypted_data)
