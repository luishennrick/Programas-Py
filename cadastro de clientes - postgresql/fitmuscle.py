from PyQt5 import uic,QtWidgets
import psycopg2


conector = psycopg2.connect(
    database='fitmuscle',
    user='postgres',
    password='pgadmin123',
    host='localhost',
    port='5432')




def jcadastro():
    cadastrofit.show()
    fit.close()

def inserir():
    nome = str(cadastrofit.lineEdit.text())
    cpf = str(cadastrofit.lineEdit_2.text())
    data = str(cadastrofit.lineEdit_3.text())
    peso = str(cadastrofit.lineEdit_4.text())
    mod = str(cadastrofit.lineEdit_5.text())
    cadastrofit.lineEdit.setText("")
    cadastrofit.lineEdit_2.setText("")
    cadastrofit.lineEdit_3.setText("")
    cadastrofit.lineEdit_4.setText("")
    cadastrofit.lineEdit_5.setText("")

    cur = conector.cursor()
    cur.execute("INSERT INTO clientes (nome,cpf,data,peso,modalidade) VALUES (%s,%s,%s,%s,%s)", (nome,cpf,data,peso,mod))
    conector.commit()



def jconsultar():
    clientesfit.show()
    fit.close()
    cur = conector.cursor()

    cur.execute("SELECT*FROM clientes")
    dado = cur.fetchall()
    clientesfit.tableWidget.setColumnCount(5)
    clientesfit.tableWidget.setRowCount(len(dado))


    for i in range(0, len(dado)):
        for j in range(0, 5):
            clientesfit.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dado[i][j])))

def consultar():
    nome = str(clientesfit.lineEdit.text())
    clientesfit.lineEdit.setText("")
    cur = conector.cursor()

    cur.execute("SELECT*FROM clientes WHERE nome LIKE %s", (nome,))
    conector.commit()
    dado1 = cur.fetchall()
    clientesfit.tableWidget.setColumnCount(5)
    clientesfit.tableWidget.setRowCount(len(dado1))

    for i in range(0, len(dado1)):
        for j in range(0, 5):
            clientesfit.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dado1[i][j])))



def deletar():
    nome = str(clientesfit.lineEdit.text())
    clientesfit.lineEdit.setText("")
    clientesfit.close()
    cur = conector.cursor()
    cur.execute("DELETE FROM clientes WHERE nome = %s", (nome,))
    conector.commit()




def voltar():
    fit.show()
    cadastrofit.close()
    clientesfit.close()



app = QtWidgets.QApplication([])
fit = uic.loadUi("fitmuscle.ui")
cadastrofit = uic.loadUi("cadastrofit.ui")
clientesfit = uic.loadUi("clientesfit.ui")
fit.pushButton.clicked.connect(jcadastro)
fit.pushButton_2.clicked.connect(jconsultar)
cadastrofit.pushButton.clicked.connect(inserir)
cadastrofit.pushButton_2.clicked.connect(voltar)
clientesfit.pushButton.clicked.connect(consultar)
clientesfit.pushButton_2.clicked.connect(voltar)
clientesfit.pushButton_3.clicked.connect(deletar)


fit.show()
app.exec()

