from PyQt5 import QtCore, QtGui, QtWidgets
from Signup import Sign




class Ui_Dialog(object):

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

    def cerrar(self, ventana1):
        Dialog.show()
        ventana1.hide()

    def crearcuenta(self):
        self.ventana1 = QtWidgets.QMainWindow()
        self.gg=Sign
        self.ui=Sign()
        self.ui.setupUi(self.ventana1)
        self.ventana1.setGeometry(280, 103,781,575)
        self.ventana1.show()
        self.ui.btn_log.clicked.connect(lambda:self.cerrar(self.ventana1))
        Dialog.hide()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 575)
        Dialog.setFixedSize(781,575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(170, 93, 441, 451))
        self.frame.setStyleSheet(".QFrame{border: 1px solid gray;\n"
"border-radius: 10px;\n"
"border-color: rgb(217, 217, 217);}\n"
" ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.txt_usr = QtWidgets.QLineEdit(self.frame)
        self.txt_usr.setEnabled(True)
        self.txt_usr.setGeometry(QtCore.QRect(60, 180, 345, 51))
        self.txt_usr.setObjectName("txt_usr")
        self.txt_usr.setPlaceholderText("Correo electrónico o Usuario")
        

        self.txt_pass = QtWidgets.QLineEdit(self.frame)
        self.txt_pass.setGeometry(QtCore.QRect(60, 256, 345, 51))
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pass.setObjectName("txt_pass")
        self.txt_pass.setPlaceholderText("Contraseña")
        



        self.btn_sgte = QtWidgets.QPushButton(self.frame)
        self.btn_sgte.setGeometry(QtCore.QRect(310, 379, 96, 31))
        self.btn_sgte.setStyleSheet(".QPushButton{\n"
        "border: 1px solid gray;\n"
        "border-radius: 5px;\n"
        "background-color: rgb(0, 120, 226);\n"
        "color: rgb(255, 255, 255);\n"
        "border-color: rgb(217, 217, 217);\n"
        "font-weight:bold;}")
        self.btn_sgte.setIconSize(QtCore.QSize(16, 16))
        self.btn_sgte.setObjectName("btn_sgte")
        self.btn_cc = QtWidgets.QPushButton(self.frame)
        self.btn_cc.setGeometry(QtCore.QRect(50, 380, 101, 29))
        self.btn_cc.setStyleSheet("color:rgb(10, 128, 255);\n"
        "font: 75 11pt \"Cantarell\";\n"
        "font-weight: bold;")
        self.btn_cc.setCheckable(False)
        self.btn_cc.setAutoDefault(True)
        self.btn_cc.setDefault(False)
        self.btn_cc.setFlat(True)
        self.btn_cc.setObjectName("btn_cc")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(196, 22, 61, 61))
        self.frame_2.setStyleSheet(".QFrame{image: url(:/newPrefix/Images-UI/LoginFotx.png);\n"
        "border: 0px;\n"
        "tabwidget.setStyleSheet(\"QTabWidget::pane { border: 0; }\");}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.lbl_info = QtWidgets.QLabel(self.frame)
        self.lbl_info.setGeometry(QtCore.QRect(59, 321, 221, 19))
        self.lbl_info.setStyleSheet("color: rgb(255, 0, 4);")
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_info.hide()
        self.lbl_tit = QtWidgets.QLabel(self.frame)
        self.lbl_tit.setGeometry(QtCore.QRect(176, 92, 111, 31))
        self.lbl_tit.setStyleSheet("color: rgb(0, 0, 0);\n"
        "font: 75 22pt \"Cantarell\";")
        self.lbl_tit.setObjectName("lbl_tit")
        self.lbl_stc = QtWidgets.QLabel(self.frame)
        self.lbl_stc.setGeometry(QtCore.QRect(136, 130, 181, 31))
        self.lbl_stc.setStyleSheet("color: rgb(0, 0, 0);\n"
        "font: 75 14pt \"Cantarell\";")
        self.lbl_stc.setObjectName("lbl_stc")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(-2, 0, 811, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(6, 5, 51, 51))
        self.frame_4.setStyleSheet("border-image: url(:/Icono/Images-UI/Icono.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(350, 9, 91, 41))
        self.label.setObjectName("label")
        self.DreamTeam = QtWidgets.QLabel(self.frame_3)
        self.DreamTeam.setGeometry(QtCore.QRect(64, 15, 141, 31))
        self.DreamTeam.setObjectName("DreamTeam")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.btn_sgte.setText(_translate("Dialog", "Siguiente"))
        self.btn_cc.setText(_translate("Dialog", "Crear cuenta"))
        self.lbl_info.setText(_translate("Dialog", "Usuario o Contraseña incorrecto"))
        self.lbl_tit.setText(_translate("Dialog", "Acceder"))
        self.lbl_stc.setText(_translate("Dialog", "Usa tu cuenta de QVer"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#959595;\">QVer</span></p></body></html>"))
        self.DreamTeam.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#d0d0d0;\">Dream Team</span></p></body></html>"))
        self.btn_sgte.clicked.connect(lambda:self.charge_confirm(self.txt_pass, self.txt_usr, self.lbl_info))
        self.btn_cc.clicked.connect(lambda:self.crearcuenta())

import xz_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
