from PyQt5 import uic, QtWidgets


def emprestimo():
    prest = int
    op = int
    emp = float(credit.lineEdit.text())
    slrio = float(credit.lineEdit_2.text())
    credit.lineEdit.setText("")
    credit.lineEdit_2.setText("")

    if credit.radioButton.isChecked():
        prest = 6
        op = 1

    elif credit.radioButton_2.isChecked():
        prest = 12
        op = 1

    elif credit.radioButton_3.isChecked():
        prest = 24
        op = 1

    elif credit.radioButton_4.isChecked():
        prest = 48
        op = 1
    else:
        credit.listWidget.addItem('Selecione a quantidade de parcelas!')

    while op == 1:
        juros: float = (emp / 100) * 50
        trintaporcento: float = (slrio / 100) * 30
        vprest: float = (emp / prest) + (juros / prest)
        # converte o valor em string
        strprest = str(vprest)

        if vprest > trintaporcento:
            credit.listWidget.addItem('Desculpe, infelizmente o valor das prestações ultrapassam sua margem.')
        else:

            credit.listWidget.addItem('Parabéns seu crédito foi aprovado!')
            credit.listWidget.addItem('O valor de suas parcelas é de:R$')
            credit.listWidget.addItem(strprest)


        break


app = QtWidgets.QApplication([])
credit = uic.loadUi("emp.ui")
credit.pushButton.clicked.connect(emprestimo)

credit.show()
app.exec()
