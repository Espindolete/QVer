from PyQt5 import QtCore, QtGui, QtWidgets
from validarcorreo import validarcorreo, verexist
from Vista import *
import pymysql
import sys





class Controlador_Login(object):
    def __init__(self): 
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.ventanalogin = Pantalla_Login()
        self.ventanalogin.setupUi(self.Dialog)
        self.function()

    def function(self):
        self.ventanalogin.btn_sgte.clicked.connect(lambda:self.charge_confirm(self.ventanalogin.txt_pass, self.ventanalogin.txt_usr, self.ventanalogin.lbl_info))
        self.ventanalogin.btn_cc.clicked.connect(lambda:Mostrar_Sign())

    def charge_confirm(self, password, user, info):
        database = open ("database.txt", "r")
        usrpass=[]
        flag=False
        for x in database:
            usrpass=usrpass+x.split(",")
        for x in usrpass:
            bk=x.replace("\n", "")
            usrpass[usrpass.index(x)]=bk
        for x in usrpass:
            try:
                if (x == user.text()) and (usrpass[usrpass.index(x)+1]==password.text()):
                    flag=True
            except Exception as e:
                pass
            try:
                if (x == user.text()) and (usrpass[usrpass.index(x)-1]==password.text()):
                    flag=True
            except Exception as e:
                pass


                
        if flag:
            info.setText("Valido")
            info.setStyleSheet("color: rgb(51, 204, 40);")
            info.show()
        else:
            user.clear()
            password.clear()
            info.setText("Usuario o contraseña incorrecto")
            info.setStyleSheet("color: rgb(255, 0, 4);")           
            info.show()
        database.close()
        #print (usrpass)
class Controlador_Signup(object):
    def __init__(self): 
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.ventanasign = Pantalla_Signup()
        self.ventanasign.setupUi(self.Dialog)
        self.function()

    def function(self):
        self.ventanasign.btn_log.clicked.connect(lambda:Mostrar_Login())
        self.ventanasign.btn_sgte.clicked.connect(lambda:self.registrar(self.ventanasign.txt_usr, self.ventanasign.txt_pass, self.ventanasign.txt_pass_con, self.ventanasign.lbl_info, self.ventanasign.txt_mail))
        self.ventanasign.checkBox.toggled.connect(lambda:self.ver(self.ventanasign.checkBox,self.ventanasign.txt_pass, self.ventanasign.txt_pass_con))
            

    def ver(self, ch, txt_pass, txt_pass_con):
        if ch.isChecked() == True:
            self.ventanasign.txt_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ventanasign.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ventanasign.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ventanasign.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)

    def limpiar(self, *args):
        for x in args:
            x.clear()

    def registrar(self, usr, password, passconf, info, mail):
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
                                    database = open("database.txt", "a")
                                    newuser=usr.text()+","+password.text()+"\n"
                                    database.write(newuser)
                                    info.setStyleSheet("color: rgb(50, 200, 40);")
                                    info.setText("Usuario registrado con exito!(Sin mail).")
                                    database.close()
                                    info.show()
                                    self.limpiar(usr, password, passconf, mail)
                                else:
                            #Con correo registrado
                                    validar=validarcorreo(mail.text())
                                    info.hide()
                                    if validar:
                                        validar=verexist(mail.text())
                                        if validar:
                                            database = open("database.txt", "a")
                                            newuser=usr.text()+","+password.text()+","+mail.text()+"\n"
                                            database.write(newuser)
                                            info.setStyleSheet("color: rgb(50, 200, 40);")
                                            info.setText("Usuario registrado con exito!.")
                                            database.close()
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

#INSTANCIA LAS PANTALLAS
LoginScreen=Controlador_Login()
SingupScreen=Controlador_Signup()


#LLAMA A LAS PANTALLAS
def Mostrar_Login():
    LoginScreen.Dialog.show()
    SingupScreen.Dialog.hide()
def Mostrar_Sign():
    LoginScreen.Dialog.hide()
    SingupScreen.Dialog.show()


#CONECTA A LA BD
def conectar(usr='', passwod='', bd=''):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user=usr,
                                 password=passwod,
                                 charset='utf8mb4',
                                 db=bd)
    return connection

#INIT DEL LOGIN
if __name__ == "__main__":
    Mostrar_Login()
    sys.exit(LoginScreen.app.exec_())
		