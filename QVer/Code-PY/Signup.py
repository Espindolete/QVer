import xz_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from validarcorreo import validarcorreo, verexist

class Sign(object):

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

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 30, 761, 521))
        self.frame.setStyleSheet(".QFrame{border: 1px solid gray;\n"
        "border-radius: 10px;\n"
        "border-color: rgb(217, 217, 217);}\n"
        " ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(450, 330, 41, 24))
        self.checkBox.setObjectName("checkBox")


        self.txt_usr = QtWidgets.QLineEdit(self.frame)
        self.txt_usr.setEnabled(True)
        self.txt_usr.setGeometry(QtCore.QRect(60, 150, 380, 51))
        self.txt_usr.setObjectName("txt_usr")
        self.txt_usr.setPlaceholderText("Nombre de usuario *")


        self.txt_pass = QtWidgets.QLineEdit(self.frame)
        self.txt_pass.setGeometry(QtCore.QRect(60, 314, 181, 51))
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pass.setObjectName("txt_pass")
        self.txt_pass.setPlaceholderText("Contraseña *")


        self.btn_sgte = QtWidgets.QPushButton(self.frame)
        self.btn_sgte.setGeometry(QtCore.QRect(310, 440, 101, 41))
        self.btn_sgte.setStyleSheet(".QPushButton{\n"
        "border: 1px solid gray;\n"
        "border-radius: 5px;\n"
        "background-color: rgb(0, 190, 250);\n"
        "color: rgb(255, 255, 255);\n"
        "border-color: rgb(217, 217, 217);\n"
        "font-weight:bold;}")
        self.btn_sgte.setIconSize(QtCore.QSize(16, 16))
        self.btn_sgte.setObjectName("btn_sgte")
        self.btn_log = QtWidgets.QPushButton(self.frame)
        self.btn_log.setGeometry(QtCore.QRect(50, 451, 211, 29))
        self.btn_log.setStyleSheet("color:rgb(10, 128, 255);\n"
        "font: 75 11pt \"Cantarell\";\n"
        "font-weight: bold;")
        self.btn_log.setCheckable(False)
        self.btn_log.setAutoDefault(True)
        self.btn_log.setDefault(False)
        self.btn_log.setFlat(True)
        self.btn_log.setObjectName("btn_log")
        self.lbl_info = QtWidgets.QLabel(self.frame)
        self.lbl_info.setGeometry(QtCore.QRect(390, 500, 361, 19))
        self.lbl_info.setStyleSheet("color: rgb(255, 0, 4);")
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_info.hide()
        self.lbl_regla1 = QtWidgets.QLabel(self.frame)
        self.lbl_regla1.setGeometry(QtCore.QRect(60, 374, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_regla1.setFont(font)
        self.lbl_regla1.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Cantarell\";")
        self.lbl_regla1.setObjectName("lbl_regla1")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(30, 20, 61, 71))
        self.frame_4.setStyleSheet("image: url(:/Icono/Images-UI/Icono.png);\n"
"border:0px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lbl_dt = QtWidgets.QLabel(self.frame)
        self.lbl_dt.setGeometry(QtCore.QRect(100, 40, 141, 31))
        self.lbl_dt.setObjectName("lbl_dt")
        self.lbl_cc = QtWidgets.QLabel(self.frame)
        self.lbl_cc.setGeometry(QtCore.QRect(60, 100, 251, 31))
        self.lbl_cc.setObjectName("lbl_cc")
        self.lbl_regla2 = QtWidgets.QLabel(self.frame)
        self.lbl_regla2.setGeometry(QtCore.QRect(60, 390, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_regla2.setFont(font)
        self.lbl_regla2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Cantarell\";")
        self.lbl_regla2.setObjectName("lbl_regla2")


        self.txt_pass_con = QtWidgets.QLineEdit(self.frame)
        self.txt_pass_con.setGeometry(QtCore.QRect(260, 314, 181, 51))
        self.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pass_con.setObjectName("txt_pass_con")
        self.txt_pass_con.setPlaceholderText("Confirmar contraseña *")
        

        self.txt_mail = QtWidgets.QLineEdit(self.frame)
        self.txt_mail.setEnabled(True)
        self.txt_mail.setGeometry(QtCore.QRect(60, 230, 380, 51))
        self.txt_mail.setObjectName("txt_mail")
        self.txt_mail.setPlaceholderText("Correo electrónico")


        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(500, 150, 241, 221))
        self.frame_2.setStyleSheet("border-image: url(:/Shield/Images-UI/QverShield.png);\n"
        "border: 0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Signup"))
        self.btn_sgte.setText(_translate("Dialog", "Siguiente"))
        self.btn_log.setText(_translate("Dialog", "Acceder a tu cuenta en su lugar"))
        self.checkBox.setText(_translate("Dialog", "☉"))
        self.lbl_info.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Datos invalidos.</p></body></html>"))
        self.lbl_regla1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Usa 8 o más caracteres con combinación de letras,</span></p></body></html>"))
        self.lbl_dt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#010101;\">Dream Team</span></p></body></html>"))
        self.lbl_cc.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#010101;\">Crea tu cuenta de QVer</span></p></body></html>"))
        self.lbl_regla2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">números y símbolos. Los campos con (*) son obligatorios.</span></p></body></html>"))
        self.btn_sgte.clicked.connect(lambda:self.registrar(self.txt_usr, self.txt_pass, self.txt_pass_con, self.lbl_info, self.txt_mail))
        self.checkBox.toggled.connect(lambda:self.ver(self.checkBox,self.txt_pass, self.txt_pass_con))
            




    

'''
def logearse(self):
    from Login import Ui_Dialog
    self.ventana = QtWidgets.QMainWindow()
    self.ui=Ui_Dialog()
    self.ui.setupUi(self.ventana)
    self.ventana.setGeometry(280, 65,781,575)
    self.ventana.show()
'''