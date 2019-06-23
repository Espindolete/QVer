# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Pantalla_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(-2, 0, 811, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.frame_4.setStyleSheet("border-image: url(:/Icono/Images-UI/Icono.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.DreamTeam = QtWidgets.QLabel(self.frame_3)
        self.DreamTeam.setGeometry(QtCore.QRect(90, 20, 201, 31))
        self.DreamTeam.setStyleSheet("font: 18pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.DreamTeam.setObjectName("DreamTeam")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(150, 80, 511, 451))
        self.frame.setStyleSheet(".QFrame{border: 1px solid gray;\n"
"border-radius: 10px;\n"
"border-color: rgb(217, 217, 217);}\n"
" ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_cc = QtWidgets.QPushButton(self.frame)
        self.btn_cc.setGeometry(QtCore.QRect(80, 380, 131, 29))
        self.btn_cc.setStyleSheet("font: 30pt \"Jurassic Park\";\n"
"color: rgb(0, 107, 161);")
        self.btn_cc.setCheckable(False)
        self.btn_cc.setAutoDefault(True)
        self.btn_cc.setDefault(False)
        self.btn_cc.setFlat(True)
        self.btn_cc.setObjectName("btn_cc")
        self.lbl_info = QtWidgets.QLabel(self.frame)
        self.lbl_info.setGeometry(QtCore.QRect(90, 330, 221, 19))
        self.lbl_info.setStyleSheet("color: rgb(255, 0, 4);")
        self.lbl_info.setObjectName("lbl_info")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(220, 110, 61, 61))
        self.frame_2.setStyleSheet(".QFrame{image: url(:/newPrefix/Images-UI/LoginFotx.png);\n"
"border: 0px;\n"
"tabwidget.setStyleSheet(\"QTabWidget::pane { border: 0; }\");}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.lbl_stc = QtWidgets.QLabel(self.frame)
        self.lbl_stc.setGeometry(QtCore.QRect(160, 50, 211, 31))
        self.lbl_stc.setStyleSheet("font: 18pt \"Avengeance\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.lbl_stc.setObjectName("lbl_stc")
        self.txt_usr = QtWidgets.QLineEdit(self.frame)
        self.txt_usr.setGeometry(QtCore.QRect(90, 200, 341, 51))
        font = QtGui.QFont()
        font.setFamily("THE GONjURING")
        font.setPointSize(16)
        self.txt_usr.setFont(font)
        self.txt_usr.setStyleSheet(".QLineEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);\n"
"\n"
"\n"
"color: rgb(255, 255, 255);}\n"
".QLineEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);\n"
"}")
        self.txt_usr.setObjectName("txt_usr")
        self.txt_pass = QtWidgets.QLineEdit(self.frame)
        self.txt_pass.setGeometry(QtCore.QRect(90, 270, 341, 51))
        font = QtGui.QFont()
        font.setFamily("THE GONjURING")
        font.setPointSize(16)
        self.txt_pass.setFont(font)
        self.txt_pass.setStyleSheet(".QLineEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);\n"
"\n"
"\n"
"color: rgb(255, 255, 255);}\n"
".QLineEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);\n"
"}")
        self.txt_pass.setObjectName("txt_pass")
        self.btn_sgte = QtWidgets.QPushButton(self.frame)
        self.btn_sgte.setGeometry(QtCore.QRect(310, 380, 111, 31))
        self.btn_sgte.setStyleSheet(".QPushButton{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 117, 175);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 26pt \"Jurassic Park\"}")
        self.btn_sgte.setObjectName("btn_sgte")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.DreamTeam.setText(_translate("Dialog", "dream team"))
        self.btn_cc.setText(_translate("Dialog", "Crear cuenta"))
        self.lbl_info.setText(_translate("Dialog", "Usuario o Contraseña incorrecto"))
        self.lbl_stc.setText(_translate("Dialog", "Usa tu cuenta de QVer"))
        self.btn_sgte.setText(_translate("Dialog", "SIGUIENTE"))

import xz_rc
