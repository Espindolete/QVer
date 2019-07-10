from PyQt5 import QtCore, QtGui, QtWidgets

from validarcorreo import validarcorreo, verexist

from Vista import *
from Modelo import Usuario

from BDConnector import *
import pymysql
import sys

import threading

#defino cosas aca para que vean cuando lo abren y porque por ahi no me detecta como global alguna variable
peliUser=list()
usuario=Usuario()
RecomendacionesQuiz=list()
RecomendacionesPerfil=list()
iterador=0


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
		self.visible=False
		self.app = QtWidgets.QApplication(sys.argv)
		self.Dialog = QtWidgets.QDialog()
		self.ventanasignup = Pantalla_Signup()
		self.ventanasignup.setupUi(self.Dialog)
		self.function()

	def ver(self, txt_pass, txt_pass_con):
		if self.visible == False:
			self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
			self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Normal)
			self.visible=True
		else:
			self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
			self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)
			self.visible=False

	def function(self):
		self.ventanasignup.btn_log.clicked.connect(lambda:Mostrar_Login())
		self.ventanasignup.btn_sgte.clicked.connect(lambda:self.registrar(self.ventanasignup.txt_usr, self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con, self.ventanasignup.lbl_info, self.ventanasignup.txt_mail))
		self.ventanasignup.ojito.clicked.connect(lambda:self.ver(self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con))


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
		self.ventanamain.botonMiPerfil.clicked.connect(lambda:Mostrar_Profile())
		#SIGUIENTE ANTERIOR BUTTONS
		self.ventanamain.anteriores.clicked.connect(lambda:self.Cambiar_Pelis(-1))
		self.ventanamain.siguientes.clicked.connect(lambda:self.Cambiar_Pelis(1))
		self.ventanamain.botonRecomendame.clicked.connect(lambda:Mostrar_Quiz())


		#PELIS
		self.ventanamain.peli1.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap1, self.id[3]))#aca deberia pasar la id de la peli
		self.ventanamain.peli2.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap2, self.id[2]))#aca deberia pasar la id de la peli
		self.ventanamain.peli3.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap3, self.id[1]))#aca deberia pasar la id de la peli
		self.ventanamain.peli4.clicked.connect(lambda:Mostrar_Info(self.ventanamain.pixmap4, self.id[0]))#aca deberia pasar la id de la peli
	
		#Recomendame
		self.ventanamain.superRecomendame.clicked.connect(lambda:Mostrar_Quiz())

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

	def TransicionarAMain(self,func):
		flag=False
		decision=[]
		decision.append(InfoScreen.info.idPeli)
		
		if(InfoScreen.info.r_dislike.isChecked()==True):
			if(len(peliUser)>0):
				for peli in peliUser:
					if(InfoScreen.info.idPeli==peli[0]):
						peli[1]=-1
						update(peli[0],usuario.getId(),-1)
						flag=True
						break
			if flag==False:
				decision.append(-1)
				insert(InfoScreen.info.idPeli,usuario.getId(),-1)
				peliUser.append(decision)
		elif(InfoScreen.info.r_like.isChecked()==True):
			if(len(peliUser)>0):
				for peli in peliUser:
					if(InfoScreen.info.idPeli==peli[0]):
						peli[1]=1
						update(peli[0],usuario.getId(),1)
						flag=True
						break
			if flag==False:
				decision.append(1)
				insert(InfoScreen.info.idPeli,usuario.getId(),1)
				peliUser.append(decision)
		func

	def function(self):
		pass
		self.info.label.clicked.connect(lambda:self.TransicionarAMain(Mostrar_Main()))
		self.info.perfil.clicked.connect(lambda:self.TransicionarAMain(Mostrar_Profile()))
		self.info.label_2.clicked.connect(lambda:Mostrar_Quiz())
		#self.info.anteriores.clicked.connect(lambda:Cambiar_Pelis(-1))
		#self.info.siguientes.clicked.connect(lambda:Cambiar_Pelis(1))
		#self.ventanasign.checkBox.toggled.connect(lambda:self.ver(self.ventanasign.checkBox,self.ventanasign.txt_pass, self.ventanasign.txt_pass_con))

class controlador_Quiz(object):
	def __init__(self): 
		self.app = QtWidgets.QApplication(sys.argv)
		self.Dialog = QtWidgets.QDialog()
		self.quiz = Pantalla_Quiz()
		self.quiz.setupUi(self.Dialog)
		self.id=0		
		self.function()
		hilo1 = threading.Thread(name='chequear', 
                         target=self.cargarpelis,
                         daemon=True)
		hilo1.start()


	#Cada que sea llamada cargara la siguiente pelicula y asi sucesivamente
	def cargarpelis(self):
		try:	
			#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
			registro=pelis[self.id-1]
			#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
			URI= registro[6]
			self.url=urllib.request.urlopen(URI).read()
			self.quiz.pixmap.loadFromData(self.url)
			self.quiz.label_4.setPixmap(self.quiz.pixmap)
			
		except Exception as e:
			print("Maximo de peliculas cargadas")
		
	def like(self, id=0):
		insert(id,usuario.getId(),1)
		self.id=aumentarIterador()
		self.cargarpelis()
	def dislike(self, id=0):
		insert(id,usuario.getId(),-1)
		self.id=aumentarIterador()
		self.cargarpelis()
	def novi(self, id=0):
		insert(id,usuario.getId(),0)
		self.id=aumentarIterador()
		self.cargarpelis()

	def function(self):
		self.cargarpelis()
		self.quiz.inicio.clicked.connect(lambda:Mostrar_Main())
		self.quiz.miperfil.clicked.connect(lambda:Mostrar_Profile())
		self.quiz.likebtn.clicked.connect(lambda:self.like(self.id))
		self.quiz.dislikebtn.clicked.connect(lambda:self.dislike(self.id))
		self.quiz.novibtn.clicked.connect(lambda:self.novi(self.id))
		#self.info.anteriores.clicked.connect(lambda:Cambiar_Pelis(-1))
		#self.info.siguientes.clicked.connect(lambda:Cambiar_Pelis(1))
		#self.ventanasign.checkBox.toggled.connect(lambda:self.ver(self.ventanasign.checkBox,self.ventanasign.txt_pass, self.ventanasign.txt_pass_con))

#Vas a tener que implementar un nuevo definirpelismg, un nuevo siguientemg, anteriormg. COPYPASTEA NOMAS
class controlador_My_Profile(object):
	def __init__(self): 
		self.app = QtWidgets.QApplication(sys.argv)
		self.limite=0# ACA TENES QUE CREAR EN BD UNA VARIABLE pelisrec QUE CONTENGA LAS RECOMENDADAS
		self.posicion = 0 #Esta es la id inicial que carga en el main menu
		self.id=[0,1,2,3]


		self.limitemg=0 # ACA TENES QUE CREAR EN BD UNA VARIABLE pelismg QUE CONTENGA LAS GUSTADAS
		self.posicionmg = 0 #Esta es la id inicial que carga en el main menu
		self.idmg=[0,1,2,3]
		self.Dialog = QtWidgets.QDialog()
		self.profile = Pantalla_My_Profile()
		self.profile.setupUi(self.Dialog)
		'''
		hilo1 = threading.Thread(name='chequear', 
                         target=self.definirpelis,
                         args=(self.profile.pixmap1, self.profile.pixmap2, self.profile.pixmap3, self.profile.pixmap4,),
                         daemon=True)
		hilo1.start()
'''
		self.function()

	def definirpelis(self, *args):
		args=args[::-1]
		for x in args:
				self.id[args.index(x)]=peliUser[self.posicion][0]-1
				#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
				registro=pelis[peliUser[self.posicion][0]-1]
				self.posicion=self.posicion+1
				#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
				URI= registro[6]
				self.url=urllib.request.urlopen(URI).read()
				x.loadFromData(self.url)

				try:
					self.profile.peli1.setPixmap(args[3])
					self.profile.peli2.setPixmap(args[2])
					self.profile.peli3.setPixmap(args[1])
					self.profile.peli4.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.profile.peli4.setPixmap(args[0])
					self.profile.peli3.setPixmap(args[1])
					self.profile.peli2.setPixmap(args[2])
					self.profile.peli1.setPixmap(args[3])
				except Exception as e:
					pass
				
	def siguiente(self, *args):
		args=args[::-1]
		if self.posicion<=self.limite:
			for x in args:
				if self.posicion<=self.limite:
					print(self.posicion)
					self.id[args.index(x)]=peliUser[self.posicion][0]-1
					#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
					registro=pelis[peliUser[self.posicion][0]-1]
					#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
					URI= registro[6]
					self.url=urllib.request.urlopen(URI).read()
					x.loadFromData(self.url)
					if self.posicion==self.limite:
						break
					self.posicion=self.posicion+1
				try:
					self.profile.peli1.setPixmap(args[3])
					self.profile.peli2.setPixmap(args[2])
					self.profile.peli3.setPixmap(args[1])
					self.profile.peli4.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.profile.peli4.setPixmap(args[0])
					self.profile.peli3.setPixmap(args[1])
					self.profile.peli2.setPixmap(args[2])
					self.profile.peli1.setPixmap(args[3])
				except Exception as e:
					pass

	def anterior(self, *args):
		args=args[::-1]
		if self.posicion>=0:
			for x in args:
				if self.posicion>0:
					self.id[args.index(x)]=peliUser[self.posicion][0]-1
					#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
					registro=pelis[peliUser[self.posicion][0]-1]
					self.posicion=self.posicion-1
					#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
					URI= registro[6]
					self.url=urllib.request.urlopen(URI).read()
					x.loadFromData(self.url)
				try:
					self.profile.peli1.setPixmap(args[3])
					self.profile.peli2.setPixmap(args[2])
					self.profile.peli3.setPixmap(args[1])
					self.profile.peli4.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.profile.peli4.setPixmap(args[0])
					self.profile.peli3.setPixmap(args[1])
					self.profile.peli2.setPixmap(args[2])
					self.profile.peli1.setPixmap(args[3])
				except Exception as e:
					pass
			
	def definirpelismg(self, *args):
		print("xd")
		print(RecomendacionesPerfil[self.posicion])
		print("xd")
		args=args[::-1]
		for x in args:
				print(self.posicion)
				self.idmg[args.index(x)]=RecomendacionesPerfil[self.posicionmg]-1
				#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
				registro=pelis[RecomendacionesPerfil[self.posicionmg]-1]
				self.posicionmg=self.posicionmg+1
				#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
				URI= registro[6]
				self.url=urllib.request.urlopen(URI).read()
				x.loadFromData(self.url)

				try:
					self.profile.peli1mg.setPixmap(args[3])
					self.profile.peli2mg.setPixmap(args[2])
					self.profile.peli3mg.setPixmap(args[1])
					self.profile.peli4mg.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.profile.peli4mg.setPixmap(args[0])
					self.profile.peli3mg.setPixmap(args[1])
					self.profile.peli2mg.setPixmap(args[2])
					self.profile.peli1mg.setPixmap(args[3])
				except Exception as e:
					pass
				
	def siguientemg(self, *args):
		print(RecomendacionesPerfil)
		args=args[::-1]
		if self.posicionmg<=self.limitemg:
			for x in args:
				if self.posicionmg<=self.limitemg:
					print(self.posicionmg)
					self.idmg[args.index(x)]=RecomendacionesPerfil[self.posicionmg]-1
					#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
					registro=pelis[RecomendacionesPerfil[self.posicionmg]-1]
					
					#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
					URI= registro[6]
					self.url=urllib.request.urlopen(URI).read()
					x.loadFromData(self.url)
					if self.posicionmg==self.limitemg:
						break
					self.posicionmg=self.posicionmg+1
				try:
					self.profile.peli1mg.setPixmap(args[3])
					self.profile.peli2mg.setPixmap(args[2])
					self.profile.peli3mg.setPixmap(args[1])
					self.profile.peli4mg.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.profile.peli4mg.setPixmap(args[0])
					self.profile.peli3mg.setPixmap(args[1])
					self.profile.peli2mg.setPixmap(args[2])
					self.profile.peli1mg.setPixmap(args[3])
				except Exception as e:
					pass

				

	def anteriormg(self, *args):
		print(RecomendacionesPerfil[self.posicion])
		args=args[::-1]
		if self.posicionmg>=0:
			for x in args:
				if self.posicionmg>0:
					print(self.posicionmg)
					self.idmg[args.index(x)]=RecomendacionesPerfil[self.posicionmg]-1
					#pelis llama de BDconector a la bd a un fetchall que contiene las rows de peliculas en qver BD
					registro=pelis[RecomendacionesPerfil[self.posicionmg]-1]
					self.posicionmg=self.posicionmg-1
					#registro tiene 1 registro de la bd contiene: Idpeli nombre genero año tags descripcion igm
					URI= registro[6]
					self.url=urllib.request.urlopen(URI).read()
					x.loadFromData(self.url)
				try:
					self.profile.peli1mg.setPixmap(args[3])
					self.profile.peli2mg.setPixmap(args[2])
					self.profile.peli3mg.setPixmap(args[1])
					self.profile.peli4mg.setPixmap(args[0])
				except Exception as e:
					pass
				try:
					self.profile.peli4mg.setPixmap(args[0])
					self.profile.peli3mg.setPixmap(args[1])
					self.profile.peli2mg.setPixmap(args[2])
					self.profile.peli1mg.setPixmap(args[3])
				except Exception as e:
					pass
			



	def function(self):
		self.profile.botonRecomendame.clicked.connect(lambda:Mostrar_Quiz())

		#SIGUIENTE ANTERIOR BUTTONS DE RECOMENDADAS
		self.profile.anteriores.clicked.connect(lambda:self.Cambiar_Pelis(-1))
		self.profile.siguientes.clicked.connect(lambda:self.Cambiar_Pelis(1))

		#PELIS RECOMENDADAS
		self.profile.peli1.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap1, self.id[3]))#aca deberia pasar la id de la peli
		self.profile.peli2.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap2, self.id[2]))#aca deberia pasar la id de la peli
		self.profile.peli3.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap3, self.id[1]))#aca deberia pasar la id de la peli
		self.profile.peli4.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap4, self.id[0]))#aca deberia pasar la id de la peli

	#---------------------------------------------------------------------------------------------------------------------

		#SIGUIENTE ANTERIOR BUTTONS DE GUSTADAS
		self.profile.anterioresmg.clicked.connect(lambda:self.Cambiar_Pelismg(-1))
		self.profile.siguientesmg.clicked.connect(lambda:self.Cambiar_Pelismg(1))

		#PELIS GUSTADAS
		self.profile.peli1mg.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap1mg, self.idmg[3]))#aca deberia pasar la id de la peli
		self.profile.peli2mg.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap2mg, self.idmg[2]))#aca deberia pasar la id de la peli
		self.profile.peli3mg.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap3mg, self.idmg[1]))#aca deberia pasar la id de la peli
		self.profile.peli4mg.clicked.connect(lambda:Mostrar_Info(self.profile.pixmap4mg, self.idmg[0]))#aca deberia pasar la id de la peli

	def hileramg(self, accion):
		if accion == 1 and self.posicion < self.limite:
			self.siguientemg(self.profile.pixmap1mg, self.profile.pixmap2mg, self.profile.pixmap3mg, self.profile.pixmap4mg)
		if accion == -1 and self.posicion > 0:
			self.anteriormg(self.profile.pixmap1mg, self.profile.pixmap2mg, self.profile.pixmap3mg, self.profile.pixmap4mg)

	def hilera(self, accion):
		if accion == 1 and self.posicion < self.limitemg:
			self.siguiente(self.profile.pixmap1, self.profile.pixmap2, self.profile.pixmap3, self.profile.pixmap4)
		if accion == -1 and self.posicion > 0:
			self.anterior(self.profile.pixmap1, self.profile.pixmap2, self.profile.pixmap3, self.profile.pixmap4)
	

	def Cambiar_Pelismg(self, accion):
		hilito = threading.Thread(name='chequear', 
                         target=self.hileramg,
                         args=(accion,),
                         daemon=True)
		hilito.start()
	def Cambiar_Pelis(self, accion):
		hilito = threading.Thread(name='chequear', 
                         target=self.hilera,
                         args=(accion,),
                         daemon=True)
		hilito.start()


#INSTANCIA LAS PANTALLAS

LoginScreen=Controlador_Login()
SingupScreen=Controlador_Signup()
MainScreen=controlador_Main_Menu()
InfoScreen=controlador_Info()
QuizScreen=controlador_Quiz()
ProfileScreen=controlador_My_Profile()

def Mostrar_Profile():
	InfoScreen.Dialog.hide()
	QuizScreen.Dialog.hide()
	MainScreen.Dialog.hide()
	ProfileScreen.Dialog.show()


#LLAMA A LAS PANTALLAS DE UNA MANERA POCO PRACTICA :v
def Mostrar_Login():
	LoginScreen.Dialog.show()
	SingupScreen.Dialog.hide()
def Mostrar_Sign():
	SingupScreen.Dialog.show()
	LoginScreen.Dialog.hide()
def Mostrar_Main():
	#consigo las variables globales SOLO POR SI ACASO(tuve errores sin esto en su momento)
	global RecomendacionesQuiz
	global iterador
	global RecomendacionesPerfil
	iterador=0
	#conseguimos las peliculas q posiblemente le gusten al usuario
	RecomendacionesPerfil=getRecomendacionesPerfil(usuario.getId())
	RecomendacionesQuiz=getRecomendacionesQuiz(usuario.getId())
	
	#seteamos cosas en las otras pantallas
	ProfileScreen.limite=len(RecomendacionesPerfil)
	ProfileScreen.limitemg=len(peliUser)
	QuizScreen.id=RecomendacionesQuiz[iterador]
	QuizScreen.cargarpelis()
	ProfileScreen.posicion=0
	ProfileScreen.posicionmg=0
	ProfileScreen.definirpelis(ProfileScreen.profile.pixmap1,ProfileScreen.profile.pixmap2,ProfileScreen.profile.pixmap3,ProfileScreen.profile.pixmap4)
	ProfileScreen.definirpelismg(ProfileScreen.profile.pixmap1mg,ProfileScreen.profile.pixmap2mg,ProfileScreen.profile.pixmap3mg,ProfileScreen.profile.pixmap4mg)



	MainScreen.Dialog.show()
	LoginScreen.Dialog.hide()
	SingupScreen.Dialog.hide()
	InfoScreen.Dialog.hide()
	QuizScreen.Dialog.hide()
	ProfileScreen.Dialog.hide()
	#esto lo hacemos para que cargue las peliculas que tenemos en RecomendacionesQuiz, sino intenta cargar cosas q no tiene q cargar
def Mostrar_Info(peli, id):
	InfoScreen.Dialog.show()
	MainScreen.Dialog.hide()
	ProfileScreen.Dialog.hide()

	#seteamos la informacion en base si el usuario ya le gusto una pelicula o no
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

def Mostrar_Quiz():
	MainScreen.Dialog.hide()
	InfoScreen.Dialog.hide()
	QuizScreen.Dialog.show()
	ProfileScreen.Dialog.hide()

#aumentamos el puntero q indica que pelicula recomendar y manejamos cuando llega al limito de la consulta
def aumentarIterador():
	global RecomendacionesQuiz
	global iterador
	if iterador<9:
		iterador=iterador+1
	else:
		iterador=0
		RecomendacionesQuiz=getRecomendacionesQuiz(usuario.getId())
	return RecomendacionesQuiz[iterador]
	


#INIT DEL LOGIN
if __name__ == "__main__":
	Mostrar_Login()
	sys.exit(LoginScreen.app.exec_())
		