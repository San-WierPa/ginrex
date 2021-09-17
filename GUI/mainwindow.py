import sys
import random
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupGUI()
        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.greet)
        self.greet()

    def setupGUI(self):
        self.resize(700, 500)
        self.move(400, 150)
        self.setWindowTitle("ginRex")
        # self.label = QLabel("Welcome to ginRex")
        # self.label.setParent(self)

    def greet(self):
        self.hello = [
            "Hallo Welt",
            "你好，世界",
            "Hei maailma",
            "Hello world",
            "Hola Mundo",
            "Привет мир",
            "Ciao mondo",
        ]
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec())
