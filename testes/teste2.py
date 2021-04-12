from PyQt5 import uic,QtWidgets



def teste():

    leitor = l1.lineEdit.text()
    l1.listWidget.addItem(leitor)
    l1.lineEdit.setText("")

app=QtWidgets.QApplication([])
l1=uic.loadUi("testen.ui")
l1.pushButton.clicked.connect(teste)


l1.show()
app.exec()