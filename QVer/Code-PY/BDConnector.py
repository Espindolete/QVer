import pymysql

#CONECTA A LA BD
def conectar(usr='', passwod='', bd=''):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user=usr,
                                 password=passwod,
                                 charset='utf8mb4',
                                 db=bd)
    return connection


conexion=conectar("root","","qver")
cursor=conexion.cursor()
cursor.execute("select * from usuario")
usuarios=cursor.fetchall()
print(cursor.fetchall())


cursor2=conexion.cursor()
cursor2.execute("select * from peliculas")
pelis=cursor2.fetchall()
print(cursor2.fetchall())


#Sentencia para XAMPP MySQL
#INSERT INTO `usuario` ( `nombre`, `contraseña`, `correo`) VALUES ("Braiunito", "42922075", "braiantablet@gmail.com")