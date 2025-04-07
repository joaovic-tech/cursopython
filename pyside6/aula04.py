# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QGridLayout,
    QMainWindow,
)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Meu primeiro QMainWindow")

botao = QPushButton("Texto do Botão")
botao.setStyleSheet("background-color: blue; color: white; font-size: 20px;")

botao2 = QPushButton("Texto do Botão 2")
botao2.setStyleSheet("background-color: red; color: white; font-size: 20px;")

botao3 = QPushButton("Texto do Botão 3")
botao3.setStyleSheet("background-color: green; color: white; font-size: 20px;")

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage("Meu slot foi chamado")


# status bar
status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem na barra")

# menu bar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Primeiro Menu")
primeira_acao = primeiro_menu.addAction("Primeira Ação")
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

window.show()
app.exec()
