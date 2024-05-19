import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
import lab101.closure as closure
import lab101.gen as gen
import lab101.unp as unp

class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab 10")
        self.setGeometry(100, 100, 600, 600)
        self.setStyleSheet("background-color: #6A5ACD")


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Unpack button and input
        unpack_layout = QHBoxLayout()
        unpack_input = QLineEdit()
        unpack_button = QPushButton('Unpack')
        unpack_button.clicked.connect(lambda: self.show_message(unp.unp(eval(unpack_input.text()))))
        unpack_layout.addWidget(unpack_input)
        unpack_layout.addWidget(unpack_button)
        layout.addLayout(unpack_layout)

        # Func button and input
        func_layout = QHBoxLayout()
        func_input = QLineEdit()
        func_button = QPushButton('Func')
        func_button.clicked.connect(lambda: self.show_message(unp.func(int(func_input.text()))))
        func_layout.addWidget(func_input)
        func_layout.addWidget(func_button)
        layout.addLayout(func_layout)

        # Generator button
        g = gen.prime_num()
        generator_button = QPushButton('Generator')
        generator_button.clicked.connect(lambda: self.show_message(next(g)))
        layout.addWidget(generator_button)

        fread_layout = QHBoxLayout()
        fread_input = QLineEdit()
        fread_button = QPushButton('Fread')
        self.reader = None
        fread_button.clicked.connect(lambda: self.read_file(fread_input.text()))
        fread_layout.addWidget(fread_input)
        fread_layout.addWidget(fread_button)
        layout.addLayout(fread_layout)

    def read_file(self, filename):
        if self.reader is None:
            self.reader = closure.fread(filename)
        try:
            line = self.reader()
            self.show_message(line)
        except StopIteration:
            self.show_message("End of file reached.")
            self.reader = None

    def show_message(self, message):
        msgBox = QMessageBox()
        msgBox.setText(repr(message))
        msgBox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = SimpleApp()
    mainWindow.show()
    sys.exit(app.exec_())
