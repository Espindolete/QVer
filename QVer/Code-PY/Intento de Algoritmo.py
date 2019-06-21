from Modelo import *


#haciendo datos falsos
agustin=Usuario("agus","agus@tin.com","tupapa")
usuarios=list()
usuarios.append(agustin)

mrsMarvel=Pelicula("capitana marvel","accion","2019","es una piba q consigue superpoderes","no tengo","a","b","c")

agustin.gustarPeli(mrsMarvel,MEGUSTA)

for usuario in usuarios:
	pelis=usuario.getPeliculas()
	nombre=usuario.getNombre()
	
	#print(pelis.getNombre())
	for peli in pelis:
		print(peli)


