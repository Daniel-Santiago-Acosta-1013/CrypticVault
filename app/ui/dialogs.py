from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class KeyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Encryption Key')

        layout = QVBoxLayout()

        self.label = QLabel('Enter the encryption key:')
        layout.addWidget(self.label)

        self.key_field = QLineEdit()
        layout.addWidget(self.key_field)

        self.button = QPushButton('OK')
        self.button.clicked.connect(self.accept)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_key(self):
        return self.key_field.text()