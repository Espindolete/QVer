from PyQt5 import QtCore, QtGui, QtWidgets

from validarcorreo import validarcorreo, verexist

from Vista import *
from Modelo import Usuario

from BDConnector import *
import pymysql
import sys

import threading

peliUser=list()
usuario=Usuario()
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
			Sesion= Usuario(Datos[0],Datos[1], Datos[2], Datos[3])
			usuario.newUser(Sesion)
			getPelisUsuario(usuario.getId(),peliUser)
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
		self.limite=len(pelis)-1
		self.posicion = -1 #Esta es la id inicial que carga en el main menu
		self.id=[0,1,2,3]
		self.Dialog = QtWidgets.QDialog()
		self.ventanamain = Pantalla_Main_Menu()
		self.ventanamain.setupUi(self.Dialog)
		hilo1 = threading.Thread(name='chequear', 
                         target=self.definirpelis,
                         args=(self.ventanamain.pixmap1, self.ventanamain.pixmap2, self.ventanamain.pixmap3, self.ventanamain.pixmap4,),
                         daemon=True)
		hilo1.start()
		self.function()

	def definirpelis(self, *args):
		args=args[::-1]
		for x in args:
				self.posicion=self.posicion+1
				self.id[args.index(x)]=self.posicion
				#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
				registro=pelis[self.posicion]
				#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
				URI= registro[6]
				self.url=urllib.request.urlopen(URI).read()
				x.loadFromData(self.url)

				try:
					self.ventanamain.peli1.setPixmap(args[3])
					self.ventanamain.peli2.setPixmap(args[2])
					self.ventanamain.peli3.setPixmap(args[1])
					self.ventanamain.peli4.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.ventanamain.peli4.setPixmap(args[0])
					self.ventanamain.peli3.setPixmap(args[1])
					self.ventanamain.peli2.setPixmap(args[2])
					self.ventanamain.peli1.setPixmap(args[3])
				except Exception as e:
					pass
				

	def siguiente(self, *args):
		args=args[::-1]
		if self.posicion<=self.limite:
			for x in args:
				if self.posicion<self.limite:
					self.posicion=self.posicion+1
					self.id[args.index(x)]=self.posicion
					#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
					registro=pelis[self.posicion]
					#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
					URI= registro[6]
					self.url=urllib.request.urlopen(URI).read()
					x.loadFromData(self.url)
				try:
					self.ventanamain.peli1.setPixmap(args[3])
					self.ventanamain.peli2.setPixmap(args[2])
					self.ventanamain.peli3.setPixmap(args[1])
					self.ventanamain.peli4.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.ventanamain.peli4.setPixmap(args[0])
					self.ventanamain.peli3.setPixmap(args[1])
					self.ventanamain.peli2.setPixmap(args[2])
					self.ventanamain.peli1.setPixmap(args[3])
				except Exception as e:
					pass

				

	def anterior(self, *args):
		args=args[::-1]
		if self.posicion>=0:
			for x in args:
				if self.posicion>0:
					self.posicion=self.posicion-1
					self.id[args.index(x)]=self.posicion
					#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
					registro=pelis[self.posicion]
					#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
					URI= registro[6]
					self.url=urllib.request.urlopen(URI).read()
					x.loadFromData(self.url)
				try:
					self.ventanamain.peli1.setPixmap(args[3])
					self.ventanamain.peli2.setPixmap(args[2])
					self.ventanamain.peli3.setPixmap(args[1])
					self.ventanamain.peli4.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.ventanamain.peli4.setPixmap(args[0])
					self.ventanamain.peli3.setPixmap(args[1])
					self.ventanamain.peli2.setPixmap(args[2])
					self.ventanamain.peli1.setPixmap(args[3])
				except Exception as e:
					pass
			


	def function(self):
		#SIGUIENTE ANTERIOR BUTTONS
		self.ventanamain.anteriores.clicked.connect(lambda:self.Cambiar_Pelis(-1))
		self.ventanamain.siguientes.clicked.connect(lambda:self.Cambiar_Pelis(1))

		#PELIS
		self.ventanamain.peli1.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap1, self.id[3]))#aca deberia pasar la id de la peli
		self.ventanamain.peli2.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap2, self.id[2]))#aca deberia pasar la id de la peli
		self.ventanamain.peli3.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap3, self.id[1]))#aca deberia pasar la id de la peli
		self.ventanamain.peli4.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap4, self.id[0]))#aca deberia pasar la id de la peli
	

	def hilera(self, accion):
		if accion == 1 and self.posicion < self.limite:
			self.siguiente(self.ventanamain.pixmap1, self.ventanamain.pixmap2, self.ventanamain.pixmap3, self.ventanamain.pixmap4)
		if accion == -1 and self.posicion > 0:
			self.anterior(self.ventanamain.pixmap1, self.ventanamain.pixmap2, self.ventanamain.pixmap3, self.ventanamain.pixmap4)
	
	def Cambiar_Pelis(self, accion):
		hilito = threading.Thread(name='chequear', 
                         target=self.hilera,
                         args=(accion,),
                         daemon=True)
		hilito.start()

class controlador_Info(object):
	def __init__(self): 
		self.app = QtWidgets.QApplication(sys.argv)
		self.Dialog = QtWidgets.QDialog()
		self.info = Pantalla_Info()
		self.info.setupUi(self.Dialog)

		self.function()

	def TransicionarAMain(self):
		flag=False
		print(InfoScreen.info.idPeli)
		if(InfoScreen.info.r_dislike.isChecked()==True):
			if(len(peliUser)>0):
				for peli in peliUser:
					print(peli[0])
					if(InfoScreen.info.idPeli==peli[0]):
						update(peli[0],usuario.getId(),-1)
						flag=True
						break
			if flag==False:
				insert(InfoScreen.info.idPeli,usuario.getId(),-1)
		elif(InfoScreen.info.r_like.isChecked()==True):
			if(len(peliUser)>0):
				for peli in peliUser:
					if(InfoScreen.info.idPeli==peli[0]):
						update(peli[0],usuario.getId(),1)
						flag=True
						break
			if flag==False:
				insert(InfoScreen.info.idPeli,usuario.getId(),-1)
		Mostrar_Main()


	def function(self):
		pass
		self.info.label.clicked.connect(lambda:self.TransicionarAMain())
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
	getPelisUsuario(usuario.getId(),peliUser)

def Mostrar_Info(peli, id):
	MainScreen.Dialog.hide()
	InfoScreen.Dialog.show()

	InfoScreen.info.img_peli.setPixmap(peli)



	InfoScreen.info.r_dislike.setAutoExclusive(False)
	InfoScreen.info.r_like.setAutoExclusive(False)
	InfoScreen.info.r_dislike.setChecked(False)
	InfoScreen.info.r_like.setChecked(False)

	InfoScreen.info.r_dislike.setAutoExclusive(True)
	InfoScreen.info.r_like.setAutoExclusive(True)
	for peli in peliUser:
		if(peli[0]==pelis[id][0]):
			if(peli[1]==1):
				InfoScreen.info.r_like.setChecked(True)
			elif(peli[1]==-1):
				InfoScreen.info.r_dislike.setChecked(True)
			else:
				InfoScreen.info.r_dislike.setChecked(False)
				InfoScreen.info.r_like.setChecked(False)
		
	InfoScreen.info.idPeli=pelis[id][0]
	pelicula=pelis[id]
	InfoScreen.info.title_peli.setText(pelicula[1])
	InfoScreen.info.desc_peli.setText(pelicula[5])





#INIT DEL LOGIN
if __name__ == "__main__":
	Mostrar_Login()
	sys.exit(LoginScreen.app.exec_())
		