import sys
import pandas as pd
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

login = uic.loadUi("ventana1.ui")
entrar = uic.loadUi("ventana2.ui")
error = uic.loadUi("ventana3.ui")

login.show()

data = []  # Lista para almacenar los datos ingresados por el usuario

def gui_login():
    id = login.lineEdit.text()
    name = login.lineEdit_2.text()
    telCel = login.lineEdit_3.text()
    apellido = login.lineEdit_4.text()
    correo = login.lineEdit_5.text()

    if len(id) == 0 or len(name) == 0 or len(telCel) == 0 or len(apellido) == 0 or len(correo) == 0:
        gui_error()
    else:
        data.append([id, name, telCel, apellido, correo])  # Agregar los datos a la lista
        guardar_datos_excel(data)  # Guardar los datos en un archivo Excel
        gui_entrar()

def guardar_datos_excel(data):
    pd.set_option('io.excel.xlsx.writer', 'openpyxl')  # Utilizar openpyxl como motor de escritura de Excel
    df = pd.DataFrame(data, columns=['ID', 'Nombre', 'Teléfono', 'Apellido', 'Correo'])
    df.to_excel('datos_usuarios.xlsx', index=False)  # Exportar DataFrame a un archivo Excel

def gui_error():
    login.hide()
    error.show()
    error.pushButton.clicked.connect(regresar_error)

def gui_entrar():
    login.hide()
    entrar.show()

def regresar_entrar():
    entrar.hide()
    login.show()

def regresar_error():
    error.hide()
    login.show()

def cerrar_ventana_entrar():
    entrar.close()

def cerrar_ventana_error():
    error.close()

login.pushButton.clicked.connect(gui_login)

entrar.pushButton.clicked.connect(cerrar_ventana_entrar)
entrar.pushButton_2.clicked.connect(regresar_entrar)


error.pushButton.clicked.connect(regresar_error)
error.pushButton_2.clicked.connect(cerrar_ventana_error)

sys.exit(app.exec())

