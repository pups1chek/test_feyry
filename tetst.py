from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget ,QButtonGroup, QHBoxLayout, QVBoxLayout , QGroupBox,QRadioButton,QPushButton, QLabel

app = QApplication([])

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('какая ты фея?')


window.resize(400,300)
window.show()

app.exec()
