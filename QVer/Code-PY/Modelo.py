#hacer las variables privadas en serio

#la clase controlador se fija en el algoritmo



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

	def calificarPeli(self,peli,resp):
		self.respuestas.append(respuesta(peli,resp))

	def modificarCalificacion(self,peli,resp):
		for x in respuestas:
			if(x.peli.getNombre()==peli.getNombre):
				x.setRespuesta(resp)



	



#esto no se refleja con la base de datos
#estoy pensando en cambiar esto en un futuro para hacer mas facil el desarrollo del algoritmo
class respuesta(object):
	def __init__(self, pelicula,respuesta):
		self.pelicula=pelicula#si usaramos por id se reduciria la complejidad pero se complejaria el codeo
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
	#copiar y pega rpor cada atributo xd
