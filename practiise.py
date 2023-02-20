# import the componets we need
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle(' This is  Cool ')
button = QPushButton()
button.setText("Press Me ")
window.setCentralWidget(button)

window.show()

app.exec()
