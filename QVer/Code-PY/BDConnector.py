import pymysql

#CONECTA A LA BD
def conectar(usr='', passwod='', bd=''):
    # Connect to the database
    #PARA EJECUCION EL LOCAL CAMBIAR HOST A host='localhost' y eliminar port=3306
    connection = pymysql.connect(host='192.168.42.85',
    							 port=3306,
                                 user=usr,
                                 password=passwod,
                                 charset='utf8mb4',
                                 db=bd)
    return connection


conexion=conectar("agus","agus123","qver")
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
		request.append(peli)

def update(idpeli,idusuario,decision):
	cursor3=conexion.cursor()
	Query= "UPDATE relacionusuariopelis set calificacion ="+str(decision)+" where idusuario="+str(idusuario)+" and IdPeli="+str(idpeli)
	print(Query)
	cursor3.execute(Query)
	conexion.commit()

def insert(idpeli,idusuario,decision):
	cursor3=conexion.cursor()
	Query= "INSERT INTO relacionusuariopelis (idRelacion, IdUsuario, IdPeli, calificacion) VALUES (NULL,'"+str(idusuario)+" ', '"+str(idpeli)+"', '"+str(decision)+"')"
	print(Query)
	cursor3.execute(Query)
	conexion.commit()
	
	

#Sentencia para XAMPP MySQL
#INSERT INTO `usuario` ( `nombre`, `contraseña`, `correo`) VALUES ("Braiunito", "42922075", "braiantablet@gmail.com")