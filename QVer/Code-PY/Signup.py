
'''
    def ver(self, ch, txt_pass, txt_pass_con):
        if ch.isChecked() == True:
            self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)

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
''' 



    

'''
def logearse(self):
    from Login import Ui_Dialog
    self.ventana = QtWidgets.QMainWindow()
    self.ui=Ui_Dialog()
    self.ui.setupUi(self.ventana)
    self.ventana.setGeometry(280, 65,781,575)
    self.ventana.show()
'''