# pip uninstall PyQt5
# pip install PyQt5
# pip uninstall PyQt5 pyqt5-tools
# pip install PyQt5 pyqt5-tools
# pip install --upgrade PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit
import lab101.closure as closure
import lab101.gen as gen
import lab101.unp as unp

class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lab10")
        self.setGeometry(100, 100, 600, 600)

        self.button = QPushButton('Unpack', self)
        self.button.move(50, 70)
        self.button.clicked.connect(
            lambda: self.show_message(unp.unp([123, "asd", [1, 2, 3]])))

        self.label = QLabel('Unpack', self)
        self.label.move(50, 30)

        self.button = QPushButton('Func', self)
        self.button.move(200, 70)
        self.button.clicked.connect(lambda: self.show_message(unp.func(5)))

        self.label = QLabel('Calculate', self)
        self.label.move(200, 30)

        g = gen.prime_num()

        self.button = QPushButton('Generator', self)
        self.button.move(50, 210)
        self.button.clicked.connect(lambda: self.show_message(next(g)))

        self.label = QLabel('Get Next', self)
        self.label.move(50, 170)

        with open("my_file.txt", "w") as f:
            f.write("Hello World!")

        reader = closure.fread("my_file.txt")
        self.button = QPushButton('Fread', self)
        self.button.move(50, 350)
        self.button.clicked.connect(lambda: self.show_message(reader()))

        self.label = QLabel('Read file', self)
        self.label.move(50, 310)

    def show_message(self, message):
        msgBox = QMessageBox()
        msgBox.setText(repr(message))
        msgBox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = SimpleApp()
    mainWindow.show()
    sys.exit(app.exec_())
