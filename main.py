from PyQt5.QtWidgets import QApplication
from .ui.main_window import MainWindow

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()