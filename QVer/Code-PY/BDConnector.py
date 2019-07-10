import pymysql

#CONECTA A LA BD
def conectar(usr='', passwod='', bd=''):
    # Connect to the database
    #PARA EJECUCION EL LOCAL CAMBIAR HOST A host='localhost' y eliminar port=3306
<<<<<<< HEAD
    connection = pymysql.connect(host='192.168.42.85',
    							 port=3306,
=======
    connection = pymysql.connect(host='localhost',
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6
                                 user=usr,
                                 password=passwod,
                                 charset='utf8mb4',
                                 db=bd)
    return connection

<<<<<<< HEAD

conexion=conectar("agus","agus123","qver")
=======
conexion=conectar("root","","aver")
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6
cursor=conexion.cursor()
cursor.execute("select * from usuario")
usuarios=cursor.fetchall()
print(cursor.fetchall())


cursor2=conexion.cursor()
cursor2.execute("select * from peliculas")
pelis=cursor2.fetchall()
print(cursor2.fetchall())

def getPelisUsuario(idusuario,request):
	cursor3=conexion.cursor()
	cursor3.execute("select idpeli,calificacion from relacionusuariopelis where idusuario="+str(idusuario))
	peliUser=cursor3.fetchall()
	for peli in peliUser:
<<<<<<< HEAD
		request.append(peli)
=======
		xd=list()
		xd.append(peli[0])
		xd.append(peli[1])
		request.append(xd)
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6

def update(idpeli,idusuario,decision):
	cursor3=conexion.cursor()
	Query= "UPDATE relacionusuariopelis set calificacion ="+str(decision)+" where idusuario="+str(idusuario)+" and IdPeli="+str(idpeli)
<<<<<<< HEAD
	print(Query)
=======
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6
	cursor3.execute(Query)
	conexion.commit()

def insert(idpeli,idusuario,decision):
	cursor3=conexion.cursor()
<<<<<<< HEAD
	Query= "INSERT INTO relacionusuariopelis (idRelacion, IdUsuario, IdPeli, calificacion) VALUES (NULL,'"+str(idusuario)+" ', '"+str(idpeli)+"', '"+str(decision)+"')"
=======
	Query= "INSERT INTO relacionusuariopelis (idRelacion, IdUsuario, IdPeli, calificacion) VALUES (NULL,"+str(idusuario)+" , "+str(idpeli)+", "+str(decision)+")"
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6
	print(Query)
	cursor3.execute(Query)
	conexion.commit()
	
<<<<<<< HEAD
	
=======

#recomendaciones1 te consigue las peliculas que no hayas dado feedback q te puedan gustar
#y recomendaciones2 te consigue las peliculas que te puedan gustar (aca incluyendo si no la viste)

def getRecomendacionesPerfil(IdUsuario):
	cursor3=conexion.cursor()
	Query= "call recomendacionPerfil("+str(IdUsuario)+")"
	cursor3.execute(Query)
	aber=cursor3.fetchall()
	xd=list()
	for abersito in aber:
		xd.append(abersito[0])
	return xd


def getRecomendacionesQuiz(IdUsuario):
	cursor3=conexion.cursor()
	Query= "call recomendacionQuiz("+str(IdUsuario)+")"
	cursor3.execute(Query)
	aber=cursor3.fetchall()
	xd=list()
	for abersito in aber:
		xd.append(abersito[0])
	return xd
>>>>>>> bfe13c156e38cc92e8b4342583966364af439aa6

#consulta para las recomendaciones
'''
donde dice sesion cambiar por el usuario que queres
SELECT idpeliculas from peliculas
LEFT JOIN
	(select sum(val) valor,idpeli from 
		(SELECT IdPeli,tabla2.val,idusuario,calificacion from relacionusuariopelis
		INNER JOIN
		        (SELECT count(*) val,relacionusuariopelis.IdUsuario us from relacionusuariopelis
		        INNER JOIN
		                (SELECT * from relacionusuariopelis
		                WHERE IdUsuario=sesion
		                and Calificacion <> 0)objetivo
		        on objetivo.idPeli=relacionusuariopelis.IdPeli
		        AND objetivo.calificacion=relacionusuariopelis.Calificacion
		        WHERE relacionusuariopelis.IdUsuario<>sesion
		        GROUP by relacionusuariopelis.IdUsuario) tabla2
		on tabla2.us=relacionusuariopelis.IdUsuario) xd
	WHERE xd.calificacion=1
	group by idpeli , calificacion) tablafinal
ON tablafinal.idpeli=peliculas.idpeliculas
where idpeliculas not in 
	(SELECT idpeli from relacionusuariopelis
    where idusuario=sesion
    and calificacion<>0)
order by tablafinal.valor DESC
limit 10
'''
#Sentencia para XAMPP MySQL
#INSERT INTO `usuario` ( `nombre`, `contraseña`, `correo`) VALUES ("Braiunito", "42922075", "braiantablet@gmail.com")