from PyQt5 import QtCore, QtGui, QtWidgets

from validarcorreo import validarcorreo, verexist

from Vista import *
from Modelo import Usuario

from BDConnector import *
import pymysql
import sys


class Controlador_Login(object):
	def __init__(self): 
		self.app = QtWidgets.QApplication(sys.argv)
		self.Dialog = QtWidgets.QDialog()
		self.ventanalogin = Pantalla_Login()
		self.ventanalogin.setupUi(self.Dialog)
		self.function()
		self.Dialog.show()

	def function(self):
		self.ventanalogin.btn_sgte.clicked.connect(lambda:self.charge_confirm(self.ventanalogin.txt_pass, self.ventanalogin.txt_usr, self.ventanalogin.lbl_info))
		self.ventanalogin.btn_cc.clicked.connect(lambda:self.gotosign())


	def function(self):
		self.ventanalogin.btn_sgte.clicked.connect(lambda:self.charge_confirm(self.ventanalogin.txt_pass, self.ventanalogin.txt_usr, self.ventanalogin.lbl_info))
		self.ventanalogin.btn_cc.clicked.connect(lambda:Mostrar_Sign())


	#Accedes a la APP y guardas tu sesion
	def charge_confirm(*args):
		Datos=Usuario().logearse(args[1], args[2], args[3])
		if Datos != None:
			Sesion=Usuario(Datos[1], Datos[2], Datos[3])
			Mostrar_Main()

	def cerrar(self, ventana1):
		self.Dialog.show()
		ventana1.hide()

	def gotosign(self):
		self.crearcuenta = QtWidgets.QMainWindow()
		self.ui=Pantalla_Signup()
		self.ui.setupUi(self.crearcuenta)
		self.crearcuenta.setGeometry(293, 77,781,575)
		self.crearcuenta.show()
		self.ui.btn_log.clicked.connect(lambda:self.cerrar(self.crearcuenta))
		self.Dialog.hide()

class Controlador_Signup(object):
	def __init__(self): 
		self.app = QtWidgets.QApplication(sys.argv)
		self.Dialog = QtWidgets.QDialog()
		self.ventanasignup = Pantalla_Signup()
		self.ventanasignup.setupUi(self.Dialog)
		self.function()

	def ver(self, ch, txt_pass, txt_pass_con):
		if ch.isChecked() == True:
			self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
			self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Normal)
		else:
			self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
			self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)

	def function(self):
		self.ventanasignup.btn_log.clicked.connect(lambda:Mostrar_Login())
		self.ventanasignup.btn_sgte.clicked.connect(lambda:self.registrar(self.ventanasignup.txt_usr, self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con, self.ventanasignup.lbl_info, self.ventanasignup.txt_mail))
		self.ventanasignup.checkBox.toggled.connect(lambda:self.ver(self.ventanasignup.checkBox,self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con))


	def registrar(*args):
		Usuario().validar_registro(args[1], args[2], args[3], args[4], args[5])

class controlador_Main_Menu(object):
	def __init__(self): 
		self.app = QtWidgets.QApplication(sys.argv)
		self.Dialog = QtWidgets.QDialog()
		self.ventanamain = Pantalla_Main_Menu()
		self.ventanamain.setupUi(self.Dialog)
		self.definirpelis(self.ventanamain.pixmap1, self.ventanamain.pixmap2, self.ventanamain.pixmap3, self.ventanamain.pixmap4)
		self.function()

	def definirpelis(self, *args):
		for x in args:
			registro=pelis[args.index(x)]
			URI= registro[6]
			print(URI)
			self.url=urllib.request.urlopen(URI).read()
			x.loadFromData(self.url)

	
		self.ventanamain.peli1.setPixmap(args[0])
		self.ventanamain.peli2.setPixmap(args[1])
		self.ventanamain.peli3.setPixmap(args[2])
		self.ventanamain.peli4.setPixmap(args[3])

	def function(self):
		#SIGUIENTE ANTERIOR BUTTONS
		self.ventanamain.anteriores.clicked.connect(lambda:Cambiar_Pelis(-1))
		self.ventanamain.siguientes.clicked.connect(lambda:Cambiar_Pelis(1))

		#PELIS
		self.ventanamain.peli1.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap1, 0))#aca deberia pasar la id de la peli
		self.ventanamain.peli2.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap2, 1))#aca deberia pasar la id de la peli
		self.ventanamain.peli3.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap3, 2))#aca deberia pasar la id de la peli
		self.ventanamain.peli4.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap4, 3))#aca deberia pasar la id de la peli
	def CambiarPelis(self):
		pass

class controlador_Info(object):
	def __init__(self): 
		self.app = QtWidgets.QApplication(sys.argv)
		self.Dialog = QtWidgets.QDialog()
		self.info = Pantalla_Info()
		self.info.setupUi(self.Dialog)
		self.function()

	def function(self):
		pass
		self.info.label.clicked.connect(lambda:Mostrar_Main())
		#self.info.anteriores.clicked.connect(lambda:Cambiar_Pelis(-1))
		#self.info.siguientes.clicked.connect(lambda:Cambiar_Pelis(1))
		#self.ventanasign.checkBox.toggled.connect(lambda:self.ver(self.ventanasign.checkBox,self.ventanasign.txt_pass, self.ventanasign.txt_pass_con))


#INSTANCIA LAS PANTALLAS
LoginScreen=Controlador_Login()
SingupScreen=Controlador_Signup()
MainScreen=controlador_Main_Menu()
InfoScreen=controlador_Info()

#LLAMA A LAS PANTALLAS DE UNA MANERA POCO PRACTICA :v
def Mostrar_Login():
	LoginScreen.Dialog.show()
	SingupScreen.Dialog.hide()
def Mostrar_Sign():
	LoginScreen.Dialog.hide()
	SingupScreen.Dialog.show()
def Mostrar_Main():
	MainScreen.Dialog.show()
	LoginScreen.Dialog.hide()
	SingupScreen.Dialog.hide()
	InfoScreen.Dialog.hide()
def Mostrar_Info(peli, id):
	MainScreen.Dialog.hide()
	InfoScreen.Dialog.show()

	InfoScreen.info.img_peli.setPixmap(peli)

	pelicula=pelis[id]
	InfoScreen.info.title_peli.setText(pelicula[1])
	InfoScreen.info.desc_peli.setText(pelicula[5])





#INIT DEL LOGIN
if __name__ == "__main__":
	Mostrar_Login()
	sys.exit(LoginScreen.app.exec_())
		