# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Pantalla_Signup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 578)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-20, 0, 761, 581))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 4, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setStyleSheet(".QFrame{border: 1px solid gray;\n"
"border-radius: 10px;\n"
"border-color: rgb(9, 9, 9);\n"
"\n"
"background-color: rgb(4, 4, 4);}\n"
" ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_sgte = QtWidgets.QPushButton(self.frame)
        self.btn_sgte.setGeometry(QtCore.QRect(390, 500, 121, 41))
        self.btn_sgte.setStyleSheet(".QPushButton{\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 115, 173);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(217, 217, 217);\n"
"font: 30pt \"Jurassic Park\";}\n"
"")
        self.btn_sgte.setIconSize(QtCore.QSize(16, 16))
        self.btn_sgte.setObjectName("btn_sgte")
        self.btn_log = QtWidgets.QPushButton(self.frame)
        self.btn_log.setGeometry(QtCore.QRect(60, 510, 271, 29))
        self.btn_log.setStyleSheet("color: rgb(0, 112, 168);\n"
"font: 30pt \"Jurassic Park\";\n"
"")
        self.btn_log.setCheckable(False)
        self.btn_log.setAutoDefault(True)
        self.btn_log.setDefault(False)
        self.btn_log.setFlat(True)
        self.btn_log.setObjectName("btn_log")
        self.lbl_info = QtWidgets.QLabel(self.frame)
        self.lbl_info.setGeometry(QtCore.QRect(650, 550, 101, 20))
        self.lbl_info.setStyleSheet("color: rgb(255, 0, 4);\n"
"background-color: rgb(0, 0, 0);")
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_regla1 = QtWidgets.QLabel(self.frame)
        self.lbl_regla1.setGeometry(QtCore.QRect(50, 430, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Star Jedi")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_regla1.setFont(font)
        self.lbl_regla1.setStyleSheet("font: 26pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.lbl_regla1.setObjectName("lbl_regla1")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(50, 30, 61, 71))
        self.frame_4.setStyleSheet("image: url(:/Icono/Images-UI/Icono.png);\n"
"border:0px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lbl_regla2 = QtWidgets.QLabel(self.frame)
        self.lbl_regla2.setGeometry(QtCore.QRect(50, 460, 491, 20))
        font = QtGui.QFont()
        font.setFamily("Star Jedi")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_regla2.setFont(font)
        self.lbl_regla2.setStyleSheet("font: 6pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.lbl_regla2.setObjectName("lbl_regla2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(530, 150, 231, 221))
        self.frame_2.setStyleSheet("border-image: url(:/Shield/Images-UI/QverShield.png);\n"
"border: 0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 330, 141, 16))
        self.label_2.setStyleSheet("font: 12pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(250, 330, 151, 16))
        self.label_4.setStyleSheet("font: 12pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 81, 20))
        self.label_3.setStyleSheet("\n"
"font: 12pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 150, 131, 21))
        self.label.setStyleSheet("font: 12pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.label.setObjectName("label")
        self.lbl_cc = QtWidgets.QLabel(self.frame)
        self.lbl_cc.setGeometry(QtCore.QRect(210, 100, 201, 31))
        self.lbl_cc.setStyleSheet("font: 18pt \"Avengeance\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.lbl_cc.setObjectName("lbl_cc")
        self.lbl_dt = QtWidgets.QLabel(self.frame)
        self.lbl_dt.setGeometry(QtCore.QRect(230, 40, 181, 31))
        self.lbl_dt.setStyleSheet("font: 18pt \"Star Jedi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.lbl_dt.setObjectName("lbl_dt")
        self.txt_usr = QtWidgets.QLineEdit(self.frame)
        self.txt_usr.setGeometry(QtCore.QRect(52, 190, 371, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.txt_usr.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("THE GONjURING")
        font.setPointSize(16)
        self.txt_usr.setFont(font)
        self.txt_usr.setStyleSheet(".QLineEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);\n"
"\n"
"\n"
"\n"
"background-color: rgb(0, 0, 0);}\n"
".QLineEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);\n"
"}")
        self.txt_usr.setObjectName("txt_usr")
        self.txt_mai = QtWidgets.QLineEdit(self.frame)
        self.txt_mai.setGeometry(QtCore.QRect(52, 280, 371, 31))
        font = QtGui.QFont()
        font.setFamily("THE GONjURING")
        font.setPointSize(16)
        self.txt_mai.setFont(font)
        self.txt_mai.setStyleSheet(".QLineEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);}\n"
".QLineEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);\n"
"}")
        self.txt_mai.setObjectName("txt_mai")
        self.txt_pass = QtWidgets.QLineEdit(self.frame)
        self.txt_pass.setGeometry(QtCore.QRect(50, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("THE GONjURING")
        font.setPointSize(16)
        self.txt_pass.setFont(font)
        self.txt_pass.setStyleSheet(".QLineEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}\n"
".QLineEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);\n"
"}")
        self.txt_pass.setObjectName("txt_pass")
        self.txt_pass_con = QtWidgets.QLineEdit(self.frame)
        self.txt_pass_con.setGeometry(QtCore.QRect(240, 370, 181, 31))
        font = QtGui.QFont()
        font.setFamily("THE GONjURING")
        font.setPointSize(16)
        self.txt_pass_con.setFont(font)
        self.txt_pass_con.setStyleSheet(".QLineEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);\n"
"\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);}\n"
".QLineEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);\n"
"}")
        self.txt_pass_con.setObjectName("txt_pass_con")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Signup"))
        self.btn_sgte.setText(_translate("Dialog", "Siguiente"))
        self.btn_log.setText(_translate("Dialog", "Acceder a tu cuenta en su lugar"))
        self.lbl_info.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Datos invalidos.</p></body></html>"))
        self.lbl_regla1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">usa 8 o más caracteres con combinación de letras,</span></p></body></html>"))
        self.lbl_regla2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">números y símbolos. Los campos con (✳️) son obligatorios.</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Contraseña"))
        self.label_4.setText(_translate("Dialog", "confirmación"))
        self.label_3.setText(_translate("Dialog", "Correo"))
        self.label.setText(_translate("Dialog", "usuario"))
        self.lbl_cc.setText(_translate("Dialog", "Crea tu cuenta en QVer"))
        self.lbl_dt.setText(_translate("Dialog", "Dream Team"))

import xz_rc
