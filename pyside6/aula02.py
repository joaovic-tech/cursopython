import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton("Texto do Botão")
botao.setStyleSheet("background-color: blue; color: white; font-size: 20px;")

botao2 = QPushButton("Texto do Botão 2")
botao2.setStyleSheet("background-color: red; color: white; font-size: 20px;")

botao3 = QPushButton("Texto do Botão 3")
botao3.setStyleSheet("background-color: green; color: white; font-size: 20px;")

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()


app.exec()
