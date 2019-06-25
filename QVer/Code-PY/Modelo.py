from BDConnector import *
from validarcorreo import *
import pymysql
#hacer las variables privadas en serio

#la clase controlador se fija en el algoritmo



class Usuario(object):
	def __init__(self, nombre=None,contraseña=None, correo=None):
		#id tal vez?
		self.nombre=nombre
		self.correo=correo
		self.contraseña=contraseña
		self.respuestas=list()
		#la respuesta puede ser le gusta no le gusta y no lo vi
		#so...
		#hay que hacer una clase respuesta?

	def login(self):
		pass
	def signin(self):
		pass

	def getPeliculas(self,calif):
		#aca geteamos solo las peliculas q le gustaron o no o q no vio, depende de llo q queramos
		pelis=list()
		for x in respuestas:
			if(x.getRespuesta()==calif):
				pelis.append(x.getPelicula)

		return pelis

	def gustarPeli(self,peli,resp):
		opinion=respuesta(peli,resp)
		self.respuestas.append(opinion)
		if resp==MEGUSTA:
		#añadimos el usuario a la peli para el algoritmo nms
			peli.addUsuarioPeli(self)

		if resp==NOMEGUSTA:
			print(" ")
			#se podria hacer algo
		if resp==NOLAVI:
			print(" ")
			#se podria hacer algo

	def modificarCalificacion(self,peli,resp):
		for x in respuestas:
			if(x.peli.getNombre()==peli.getNombre):
				x.setRespuesta(resp)

	def logearse(self, password, user, info):
		flag=False
		for x in usuarios:
			try:
				if (x[1] == user.text()) and (x[2]==password.text()):
					usuario=x
					flag=True
			except Exception as e:
				pass
			try:
				if (x[3] == user.text()) and (x[2]==password.text()):
					usuario=x
					flag=True
			except Exception as e:
				pass
		if flag:
			info.setText("Valido")
			info.setStyleSheet("color: rgb(51, 204, 40);")
			info.show()
			return usuario
		else:
			user.clear()
			password.clear()
			info.setText("Usuario o contraseña incorrecto")
			info.setStyleSheet("color: rgb(255, 0, 4);")           
			info.show()
			return None

	def limpiar(self, *args):
		for x in args:
			x.clear()

	def validar_registro(self, usr, password, passconf, info, mail):
		#Casos Emptys
		if len(usr.text()) == 0:
			info.setText("Campo usuario vacío.")
			info.show()
		else:
			info.hide()
			if 0 == len(password.text()):
				info.setText("Campo contraseña vacío.")
				info.show() 
			else:
				#Casos Negativos
				info.hide()
				if 3 < len(usr.text()) < 16:
					info.hide()
					if 7 < len(password.text()):
						if passconf.text() == password.text():
							#Correo opcional
							validar=verexist(usr.text())
							if validar:
								if len(mail.text())==0:
									cursor.execute("INSERT INTO `usuario`(`nombre`, `contraseña`) VALUES (%s, %s)", (usr.text(), password.text()))
									conexion.commit()
									info.setStyleSheet("color: rgb(50, 200, 40);")
									info.setText("Usuario registrado con exito!(Sin mail).")
									info.show()
									self.limpiar(usr, password, passconf, mail)
								else:
							#Con correo registrado
									validar=validarcorreo(mail.text())
									info.hide()
									if validar:
										validar=verexist(mail.text())
										if validar:
											cursor.execute("INSERT INTO `usuario`(`nombre`, `contraseña`, `correo` ) VALUES (%s, %s, %s)", (usr.text(), password.text(), mail.text()))
											conexion.commit()
											info.setStyleSheet("color: rgb(50, 200, 40);")
											info.setText("Usuario registrado con exito!.")
											info.show()
											self.limpiar(usr, password, passconf, mail)
										else:
											info.setStyleSheet("color: rgb(255, 0, 4);")
											info.setText("Ya existe un usuario regisrado con su mail.")
											info.show()
									else:
										info.setStyleSheet("color: rgb(255, 0, 4);")
										info.setText("El E-mail es invalido.")
										info.show()
							else:
								info.setStyleSheet("color: rgb(255, 0, 4);")
								info.setText("El usuario ya existe.")
								info.show()
						else:
							info.setText("Las contraseñas no coinciden.")
							info.show()    
					else:
						info.setText("Contraseña insegura, coloque más de 8 caracteres.")
						info.show()    
				else:
					info.setText("Ingrese solo nombre entre 4 y 15 caracteres.")
					info.show()
		


class respuesta(object):
	def __init__(self, pelicula,respuesta):
		self.pelicula=pelicula
		self.respuesta=respuesta

	def getPelicula(self):
		return self.pelicula
	def getNombre(self):
		return pelicula.getNombre

	def getRespuesta(self):
		return self.respuesta
	def setRespuesta(self,respuesta):
		self.respuesta=respuesta


class Pelicula:
	def __init__(self,nombre,genero,año,descripcion,img,*args):
		#id falta?
		self.nombre=nombre
		self.genero=genero
		self.año=año
		self.descripcion=descripcion
		self.img=img
		self.tags=args
		self.usuarios=list()

	def getNombre(self):
		return self.nombre
	def setNombre(self,nombre):
		self.nombre=nombre

	def getGenero(self):
		return self.genero
	def setGenero(self,genero):
		self.genero=genero

	def getAño(self):
		return self.año
	def setAño(self,año):
		self.año=año

	def getDescripcion(self):
		return self.descripcion
	def setDescripcion(self,descripcion):
		self.descripcion=descripcion

	def getImg(self):
		return self.img
	def setImg(self,img):
		self.img=img

	def getTags(self):
		return self.tags
	def setTags(self,tags):
		self.tags=tags

	def findTag(self,tag):
		for x in self.tags:
			if x==tag:
				return True
		return False


	##los ifs estos son solo para casos negativos en la degustacion de peliculas xd	
	def addUsuarioPeli(self,usuario):
		if usuario not in usuarios:
			usuarios.append(usuario)

	def removeUsuarioPeli(self,usuario):
		if usuario in usuarios:
			usuarios.remove(usuario)
		

	def getUsuariosPeli(self):
		return self.usuarios