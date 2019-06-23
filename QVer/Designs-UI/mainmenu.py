# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main - copia.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 575)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.superRecomendame = QtWidgets.QPushButton(Dialog)
        self.superRecomendame.setGeometry(QtCore.QRect(240, 440, 271, 71))
        self.superRecomendame.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(0, 100, 150);\n"
"    font: 46pt \"Jurassic Park\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.superRecomendame.setObjectName("superRecomendame")
        self.botonRecomendame = QtWidgets.QLabel(Dialog)
        self.botonRecomendame.setGeometry(QtCore.QRect(290, 40, 201, 31))
        self.botonRecomendame.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"BatmanForeverAlternate\";")
        self.botonRecomendame.setObjectName("botonRecomendame")
        self.botonMiPerfil = QtWidgets.QLabel(Dialog)
        self.botonMiPerfil.setGeometry(QtCore.QRect(520, 40, 151, 31))
        self.botonMiPerfil.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"BatmanForeverAlternate\";")
        self.botonMiPerfil.setObjectName("botonMiPerfil")
        self.botonInicio = QtWidgets.QLabel(Dialog)
        self.botonInicio.setGeometry(QtCore.QRect(180, 40, 81, 31))
        self.botonInicio.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"BatmanForeverAlternate\";")
        self.botonInicio.setObjectName("botonInicio")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 139, 741, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.anteriores = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anteriores.sizePolicy().hasHeightForWidth())
        self.anteriores.setSizePolicy(sizePolicy)
        self.anteriores.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/Images-UI/botonAnt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.anteriores.setIcon(icon)
        self.anteriores.setObjectName("anteriores")
        self.horizontalLayout.addWidget(self.anteriores)
        self.peli1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peli1.sizePolicy().hasHeightForWidth())
        self.peli1.setSizePolicy(sizePolicy)
        self.peli1.setText("")
        self.peli1.setPixmap(QtGui.QPixmap(":/pelis/Images-UI/51poKKV63GL.jpg"))
        self.peli1.setScaledContents(True)
        self.peli1.setObjectName("peli1")
        self.horizontalLayout.addWidget(self.peli1)
        self.peli2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peli2.sizePolicy().hasHeightForWidth())
        self.peli2.setSizePolicy(sizePolicy)
        self.peli2.setText("")
        self.peli2.setPixmap(QtGui.QPixmap(":/pelis/Images-UI/931823302_o.jpg"))
        self.peli2.setScaledContents(True)
        self.peli2.setObjectName("peli2")
        self.horizontalLayout.addWidget(self.peli2)
        self.peli3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peli3.sizePolicy().hasHeightForWidth())
        self.peli3.setSizePolicy(sizePolicy)
        self.peli3.setText("")
        self.peli3.setPixmap(QtGui.QPixmap(":/pelis/Images-UI/John-Wick-2-900x0-c-default.jpg"))
        self.peli3.setScaledContents(True)
        self.peli3.setObjectName("peli3")
        self.horizontalLayout.addWidget(self.peli3)
        self.peli4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peli4.sizePolicy().hasHeightForWidth())
        self.peli4.setSizePolicy(sizePolicy)
        self.peli4.setText("")
        self.peli4.setPixmap(QtGui.QPixmap(":/pelis/Images-UI/black-panther-web.jpg"))
        self.peli4.setScaledContents(True)
        self.peli4.setObjectName("peli4")
        self.horizontalLayout.addWidget(self.peli4)
        self.siguientes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.siguientes.sizePolicy().hasHeightForWidth())
        self.siguientes.setSizePolicy(sizePolicy)
        self.siguientes.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/Images-UI/botonSig.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.siguientes.setIcon(icon1)
        self.siguientes.setObjectName("siguientes")
        self.horizontalLayout.addWidget(self.siguientes)
        self.Qver = QtWidgets.QLabel(Dialog)
        self.Qver.setGeometry(QtCore.QRect(60, 40, 61, 31))
        self.Qver.setStyleSheet("font: 18pt \"Avengeance\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.Qver.setObjectName("Qver")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.superRecomendame.setText(_translate("Dialog", "RECOMENDAME"))
        self.botonRecomendame.setText(_translate("Dialog", "RECOMENDAME"))
        self.botonMiPerfil.setText(_translate("Dialog", "MI PERFIL"))
        self.botonInicio.setText(_translate("Dialog", "INICIO"))
        self.Qver.setText(_translate("Dialog", " QVer"))

import xz_rc
