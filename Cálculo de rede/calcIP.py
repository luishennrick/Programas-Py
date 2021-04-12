from PyQt5 import uic,QtWidgets


def dados():
    ip = str(lista.lineEdit.text())
    prefixo = int(lista.lineEdit_2.text())
    lista.lineEdit.setText("")
    lista.lineEdit_2.setText("")

    if prefixo == 8:
        lista.listWidget.addItem(ip)
        lista.listWidget.addItem("O endereço IP pertence a classe A!")
        lista.listWidget.addItem("A mascara padrão é 255.0.0.0")


    elif prefixo == 16:
        lista.listWidget.addItem(ip)
        lista.listWidget.addItem("O endereço IP pertence a classe B!")
        lista.listWidget.addItem("A mascara padrão é 255.255.0.0")

    while prefixo >= 24 and prefixo <= 30:

        lista.listWidget.addItem(ip)
        lista.listWidget.addItem("O endereço IP pertence a classe C!")
        lista.listWidget.addItem("Mascara de rede padrão: 255.255.255.0")

        if prefixo == 25:
            lista.listWidget.addItem("Quantidade de sub-redes: 2 ")
            lista.listWidget.addItem("Hosts válidos: 126")
            lista.listWidget.addItem("Mascara de sub-rede: 255.255.255.128 /25")

        elif prefixo == 26:
            lista.listWidget.addItem("Quantidade de sub-redes: 4 ")
            lista.listWidget.addItem("Hosts válidos: 62")
            lista.listWidget.addItem("Mascara de sub-rede: 255.255.255.192 /26")

        elif prefixo == 27:
            lista.listWidget.addItem("Quantidade de sub-redes: 8 ")
            lista.listWidget.addItem("Hosts válidos: 30")
            lista.listWidget.addItem("Mascara de sub-rede: 255.255.255.224 /27")

        elif prefixo == 28:
            lista.listWidget.addItem("Quantidade de sub-redes: 16 ")
            lista.listWidget.addItem("Hosts válidos: 14")
            lista.listWidget.addItem("Mascara de sub-rede: 255.255.255.240 /28")

        elif prefixo == 29:
            lista.listWidget.addItem("Quantidade de sub-redes: 32 ")
            lista.listWidget.addItem("Hosts válidos: 6")
            lista.listWidget.addItem("Mascara de sub-rede: 255.255.255.248 /29")

        elif prefixo == 30:
            lista.listWidget.addItem("Quantidade de sub-redes: 64 ")
            lista.listWidget.addItem("Hosts válidos: 2")
            lista.listWidget.addItem("Mascara de sub-rede: 255.255.255.252 /30")
        break

app = QtWidgets.QApplication([])
lista = uic.loadUi("calcip.ui")
lista.pushButton.clicked.connect(dados)

lista.show()
app.exec()
