# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
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
        self.txt_usr = QtWidgets.QTextEdit(self.frame)
        self.txt_usr.setEnabled(True)
        self.txt_usr.setGeometry(QtCore.QRect(60, 150, 380, 51))
        self.txt_usr.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_usr.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.txt_usr.setAcceptDrops(False)
        self.txt_usr.setAutoFillBackground(False)
        self.txt_usr.setStyleSheet(".QTextEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);}\n"
".QTextEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);}\n"
"\n"
"")
        self.txt_usr.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_usr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txt_usr.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.txt_usr.setTabChangesFocus(True)
        self.txt_usr.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txt_usr.setOverwriteMode(True)
        self.txt_usr.setAcceptRichText(False)
        self.txt_usr.setObjectName("txt_usr")
        self.txt_pass = QtWidgets.QTextEdit(self.frame)
        self.txt_pass.setGeometry(QtCore.QRect(60, 314, 181, 51))
        self.txt_pass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_pass.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.txt_pass.setAcceptDrops(False)
        self.txt_pass.setStyleSheet(".QTextEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);}\n"
".QTextEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);}\n"
"\n"
"")
        self.txt_pass.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_pass.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.txt_pass.setTabChangesFocus(True)
        self.txt_pass.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txt_pass.setOverwriteMode(True)
        self.txt_pass.setAcceptRichText(False)
        self.txt_pass.setObjectName("txt_pass")
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
        self.txt_pass_con = QtWidgets.QTextEdit(self.frame)
        self.txt_pass_con.setGeometry(QtCore.QRect(260, 314, 181, 51))
        self.txt_pass_con.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_pass_con.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.txt_pass_con.setAcceptDrops(False)
        self.txt_pass_con.setStyleSheet(".QTextEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);}\n"
".QTextEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);}\n"
"\n"
"")
        self.txt_pass_con.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_pass_con.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.txt_pass_con.setTabChangesFocus(True)
        self.txt_pass_con.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txt_pass_con.setOverwriteMode(True)
        self.txt_pass_con.setAcceptRichText(False)
        self.txt_pass_con.setObjectName("txt_pass_con")
        self.txt_mail = QtWidgets.QTextEdit(self.frame)
        self.txt_mail.setEnabled(True)
        self.txt_mail.setGeometry(QtCore.QRect(60, 230, 380, 51))
        self.txt_mail.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_mail.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.txt_mail.setAcceptDrops(False)
        self.txt_mail.setAutoFillBackground(False)
        self.txt_mail.setStyleSheet(".QTextEdit{border: 1px solid gray;\n"
"border-radius: 5px;\n"
"border-color: rgb(217, 217, 217);}\n"
".QTextEdit:focus{border: 1px solid blue;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 120, 226);}\n"
"\n"
"")
        self.txt_mail.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_mail.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txt_mail.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.txt_mail.setTabChangesFocus(True)
        self.txt_mail.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txt_mail.setOverwriteMode(True)
        self.txt_mail.setAcceptRichText(False)
        self.txt_mail.setObjectName("txt_mail")
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
        self.txt_usr.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.txt_pass.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_sgte.setText(_translate("Dialog", "Siguiente"))
        self.btn_log.setText(_translate("Dialog", "Acceder a tu cuenta en su lugar"))
        self.lbl_info.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Datos invalidos.</p></body></html>"))
        self.lbl_regla1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Usa 8 o más caracteres con combinación de letras,</span></p></body></html>"))
        self.lbl_dt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#010101;\">Dream Team</span></p></body></html>"))
        self.lbl_cc.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#010101;\">Crea tu cuenta de QVer</span></p></body></html>"))
        self.lbl_regla2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">números y símbolos. Los campos con (*) son obligatorios.</span></p></body></html>"))
        self.txt_pass_con.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.txt_mail.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import xz_rc
