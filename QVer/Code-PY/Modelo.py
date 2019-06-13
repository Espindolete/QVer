from controlador import conectar
import pymysql
#hacer las variables privadas en serio

#la clase controlador se fija en el algoritmo


coneccion=conectar("root","42922075","qver")
cur=coneccion.cursor()
cur.execute("select * from peliculas limit 1")
print(cur.fetchall())

class Usuario(object):
	def __init__(self, nombre,correo,contraseña):
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