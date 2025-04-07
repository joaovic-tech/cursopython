import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton("Texto do Botão")
botao.setStyleSheet("background-color: blue; color: white; font-size: 20px;")
botao.show()

botao2 = QPushButton("Texto do Botão 2")
botao2.setStyleSheet("background-color: red; color: white; font-size: 20px;")
botao2.show()

app.exec()
