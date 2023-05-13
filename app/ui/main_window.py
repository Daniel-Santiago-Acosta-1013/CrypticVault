from PyQt5.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog,
                             QLabel, QTabWidget, QTextEdit, QDialog)
from app.encryption.aes import encrypt, decrypt
from app.file_handlers.text_file_handler import read_file as read_text_file, write_file as write_text_file
from app.file_handlers.image_file_handler import read_file as read_image_file, write_file as write_image_file
from app.file_handlers.audio_file_handler import read_file as read_audio_file, write_file as write_audio_file
from app.file_handlers.video_file_handler import read_file as read_video_file, write_file as write_video_file
from app.ui.dialogs import KeyDialog

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enigma Machine")

        # Definir el tamaño de la ventana (ancho, alto)
        self.resize(800, 600)

        self.tab_widget = QTabWidget()

        # Crear pestañas para cada tipo de archivo
        self.text_tab = QWidget()
        self.image_tab = QWidget()
        self.audio_tab = QWidget()
        self.video_tab = QWidget()

        # Añadir las pestañas al widget de pestañas
        self.tab_widget.addTab(self.text_tab, "Texto")
        self.tab_widget.addTab(self.image_tab, "Imagen")
        self.tab_widget.addTab(self.audio_tab, "Audio")
        self.tab_widget.addTab(self.video_tab, "Video")

        # Configura la interfaz de usuario para cada pestaña
        self.text_tab_ui()
        self.image_tab_ui()
        self.audio_tab_ui()
        self.video_tab_ui()

        self.setCentralWidget(self.tab_widget)

    def text_tab_ui(self):
        layout = QVBoxLayout()

        self.encrypt_text_button = QPushButton("Encriptar Texto")
        self.encrypt_text_button.clicked.connect(self.encrypt_text_file)
        layout.addWidget(self.encrypt_text_button)

        self.decrypt_text_button = QPushButton("Desencriptar Texto")
        self.decrypt_text_button.clicked.connect(self.decrypt_text_file)
        layout.addWidget(self.decrypt_text_button)

        self.text_tab.setLayout(layout)


    def image_tab_ui(self):
        layout = QVBoxLayout()

        self.encrypt_image_button = QPushButton("Encriptar Imagen")
        self.encrypt_image_button.clicked.connect(self.encrypt_image_file)
        layout.addWidget(self.encrypt_image_button)

        self.decrypt_image_button = QPushButton("Desencriptar Imagen")
        self.decrypt_image_button.clicked.connect(self.decrypt_image_file)
        layout.addWidget(self.decrypt_image_button)

        self.image_tab.setLayout(layout)


    def audio_tab_ui(self):
        layout = QVBoxLayout()

        self.encrypt_audio_button = QPushButton("Encriptar Audio")
        self.encrypt_audio_button.clicked.connect(self.encrypt_audio_file)
        layout.addWidget(self.encrypt_audio_button)

        self.decrypt_audio_button = QPushButton("Desencriptar Audio")
        self.decrypt_audio_button.clicked.connect(self.decrypt_audio_file)
        layout.addWidget(self.decrypt_audio_button)

        self.audio_tab.setLayout(layout)


    def video_tab_ui(self):
        layout = QVBoxLayout()

        self.encrypt_video_button = QPushButton("Encriptar Video")
        self.encrypt_video_button.clicked.connect(self.encrypt_video_file)
        layout.addWidget(self.encrypt_video_button)

        self.decrypt_video_button = QPushButton("Desencriptar Video")
        self.decrypt_video_button.clicked.connect(self.decrypt_video_file)
        layout.addWidget(self.decrypt_video_button)

        self.video_tab.setLayout(layout)


    def get_file(self, title):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, title, "",
                                                  "All Files (*);;", options=options)
        return fileName


    def get_key(self):
       dialog = KeyDialog()
       result = dialog.exec()
       if result == QDialog.Accepted:
           return dialog.get_key()
       else:
           return None
       

    def encrypt_text_file(self):
        fileName = self.get_file("Seleccione el archivo de texto a encriptar")
        if fileName:
            data = read_text_file(fileName)
            key = self.get_key()
            if key:
                encrypted_data = encrypt(key, data)
                write_text_file(fileName, encrypted_data)


    def decrypt_text_file(self):
        fileName = self.get_file("Seleccione el archivo de texto a desencriptar")
        if fileName:
            data = read_text_file(fileName)
            key = self.get_key()
            if key:
                decrypted_data = decrypt(key, data)
                write_text_file(fileName, decrypted_data)


    def encrypt_image_file(self):
        fileName = self.get_file("Seleccione la imagen a encriptar")
        if fileName:
            data = read_image_file(fileName)
            key = self.get_key()
            if key:
                encrypted_data = encrypt(key, data)
                write_image_file(fileName, encrypted_data)


    def decrypt_image_file(self):
        fileName = self.get_file("Seleccione la imagen a desencriptar")
        if fileName:
            data = read_image_file(fileName)
            key = self.get_key()
            if key:
                decrypted_data = decrypt(key, data)
                write_image_file(fileName, decrypted_data)


    def encrypt_audio_file(self):
        fileName = self.get_file("Seleccione el archivo de audio a encriptar")
        if fileName:
            data = read_audio_file(fileName)
            key = self.get_key()
            if key:
                encrypted_data = encrypt(key, data)
                write_audio_file(fileName, encrypted_data)


    def decrypt_audio_file(self):
        fileName = self.get_file("Seleccione el archivo de audio a desencriptar")
        if fileName:
            data = read_audio_file(fileName)
            key = self.get_key()
            if key:
                decrypted_data = decrypt(key, data)
                write_audio_file(fileName, decrypted_data)


    def encrypt_video_file(self):
        fileName = self.get_file("Seleccione el archivo de video a encriptar")
        if fileName:
            data = read_video_file(fileName)
            key = self.get_key()
            if key:
                encrypted_data = encrypt(key, data)
                write_video_file(fileName, encrypted_data)


    def decrypt_video_file(self):
        fileName = self.get_file("Seleccione el archivo de video a desencriptar")
        if fileName:
            data = read_video_file(fileName)
            key = self.get_key()
            if key:
                decrypted_data = decrypt(key, data)
                write_video_file(fileName, decrypted_data)