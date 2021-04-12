from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

def main():

    num = int (test.lineEdit.text())
    test.lineEdit.setText("")

    if num == 1:
        test.listWidget.addItem("Teste completo")


    elif num == 2:
        test.listWidget.addItem("Teste completo")

    else:
        QMessageBox.about(test,"Alerta","número vazio ou invalido")




app=QtWidgets.QApplication([])
test=uic.loadUi("teste.ui")
test.pushButton.clicked.connect(main)


test.show()
app.exec()