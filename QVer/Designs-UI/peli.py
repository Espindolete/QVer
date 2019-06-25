# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peli.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 578)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 40, 201, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"BatmanForeverAlternate\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 40, 151, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"BatmanForeverAlternate\";")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 40, 81, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"BatmanForeverAlternate\";")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 139, 211, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_peli = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_peli.sizePolicy().hasHeightForWidth())
        self.img_peli.setSizePolicy(sizePolicy)
        self.img_peli.setText("")
        self.img_peli.setPixmap(QtGui.QPixmap("931823302_o.jpg"))
        self.img_peli.setScaledContents(True)
        self.img_peli.setObjectName("img_peli")
        self.horizontalLayout.addWidget(self.img_peli)
        self.lbl_stc = QtWidgets.QLabel(Dialog)
        self.lbl_stc.setGeometry(QtCore.QRect(60, 40, 61, 31))
        self.lbl_stc.setStyleSheet("font: 18pt \"Avengeance\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.lbl_stc.setObjectName("lbl_stc")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 410, 211, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.r_like = QtWidgets.QRadioButton(self.groupBox)
        self.r_like.setGeometry(QtCore.QRect(30, 30, 82, 17))
        self.r_like.setStyleSheet("color: rgb(0, 232, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.r_like.setObjectName("r_like")
        self.r_dislike = QtWidgets.QRadioButton(self.groupBox)
        self.r_dislike.setGeometry(QtCore.QRect(120, 30, 71, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r_dislike.sizePolicy().hasHeightForWidth())
        self.r_dislike.setSizePolicy(sizePolicy)
        self.r_dislike.setStyleSheet("color: rgb(194, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.r_dislike.setObjectName("r_dislike")
        self.desc_peli = QtWidgets.QTextEdit(Dialog)
        self.desc_peli.setEnabled(False)
        self.desc_peli.setGeometry(QtCore.QRect(260, 230, 501, 171))
        self.desc_peli.setStyleSheet("color: rgb(255, 255, 255);")
        self.desc_peli.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.desc_peli.setObjectName("desc_peli")
        self.title_peli = QtWidgets.QTextEdit(Dialog)
        self.title_peli.setEnabled(False)
        self.title_peli.setGeometry(QtCore.QRect(253, 130, 511, 81))
        self.title_peli.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.title_peli.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_peli.setLineWidth(1)
        self.title_peli.setObjectName("title_peli")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "RECOMENDAME"))
        self.label_3.setText(_translate("Dialog", "MI PERFIL"))
        self.label.setText(_translate("Dialog", "INICIO"))
        self.lbl_stc.setText(_translate("Dialog", " QVer"))
        self.r_like.setText(_translate("Dialog", "👍"))
        self.r_dislike.setText(_translate("Dialog", "👎"))
        self.desc_peli.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">era una piba q tiraba rayos con las manos y volaba muy rapido tipo superman</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
        self.title_peli.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">alguna huevada</p></body></html>"))

import xz_rc
