from Modelo import *


#haciendo datos falsos
agustin=Usuario(1,"agus","agus@tin.com","tupapa")
usuarios=list()
usuarios.append(agustin)
pelotudo=Usuario(2,"Pelo","tudo@xd.com","tudo")
usuarios.append(pelotudo)

mrsMarvel=Pelicula("capitana marvel","accion","2019","es una piba q consigue superpoderes","no tengo","a","b","c")
Daredevil=Pelicula("Daredevil","accion","2008","un pibe ciego, la Pelicula es remala","no me auerd q iba aca","a")
Frozen=Pelicula("Frozen","????","2015","frozono mujer","no me acuerdo tdv","b")
agustin.gustarPeli(mrsMarvel,MEGUSTA)
pelotudo.gustarPeli(Daredevil,NOMEGUSTA)
pelotudo.gustarPeli(mrsMarvel,MEGUSTA)
pelotudo.gustarPeli(Frozen,MEGUSTA)






	#necesito buscar de cada usuario las peliculas que le gustan
def buscarSU(usuario):
	#Buscar Usuarios Similares
	similares=list()
	multiplicador=list()
	pelis=usuario.getPeliculas(MEGUSTA)
	#de cada pelicula que le gusta al usuaro tengo q buscar otros usuarios que le gusten esas peliculas
	for peli in pelis:
		parecidos=peli.getUsuariosPeli()
		parecidos.remove(usuario)
		#mientras mas peliculas en parecido tenga el usuario mas similar al usuario es
		for usuario in parecidos:
			if usuario not in similares:
				similares.append(usuario)
				multiplicador.append(1)
			else:
				x=similares.index(usuario)
				multiplicador[x]=multiplicador[x]+1

	#aca ya tengo todos los usuarios similares encontrados y su cantidad de similitud
	return similares,multiplicador
			

similares,multi=buscarSU(agustin)
for usu in similares:
	print(usu.getNombre())