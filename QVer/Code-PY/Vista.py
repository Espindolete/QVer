from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox


from PyQt5.QtGui import *
import urllib.request
import xz_rc
from validarcorreo import validarcorreo, verexist





class QLabelClickable(QLabel):
	clicked = pyqtSignal(str)
	
	def __init__(self, parent=None):
		super(QLabelClickable, self).__init__(parent)

	def mousePressEvent(self, event):
		self.ultimo = "Clic"
	
	def mouseReleaseEvent(self, event):
		if self.ultimo == "Clic":
			QTimer.singleShot(QApplication.instance().doubleClickInterval(),
							  self.performSingleClickAction)
		else:
			# Realizar acción de doble clic.
			self.clicked.emit(self.ultimo)
	
	def mouseDoubleClickEvent(self, event):
		self.ultimo = "Doble Clic"
	
	def performSingleClickAction(self):
		if self.ultimo == "Clic":
			self.clicked.emit(self.ultimo)

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
		self.frame.setGeometry(QtCore.QRect(0, 0, 761, 581))
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
		self.lbl_info.hide()
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
		self.lbl_cc.setGeometry(QtCore.QRect(200, 100, 260, 31))
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
		font.setFamily("Arial")
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
		self.txt_mail = QtWidgets.QLineEdit(self.frame)
		self.txt_mail.setGeometry(QtCore.QRect(52, 280, 371, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(16)
		self.txt_mail.setFont(font)
		self.txt_mail.setStyleSheet(".QLineEdit{border: 1px solid gray;\n"
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
		self.txt_mail.setObjectName("txt_mail")
		self.txt_pass = QtWidgets.QLineEdit(self.frame)
		self.txt_pass.setGeometry(QtCore.QRect(50, 370, 161, 31))
		self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
		font = QtGui.QFont()
		font.setFamily("Arial")
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
		self.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)
		font = QtGui.QFont()
		font.setFamily("Arial")
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

		self.checkBox = QtWidgets.QCheckBox(self.frame)
		self.checkBox.setGeometry(QtCore.QRect(450, 375, 41, 24))
		self.checkBox.setObjectName("checkBox")
		self.checkBox.setStyleSheet(".QCheckBox{background-color: rgb(0, 0, 0);\n"
		"    color: rgb(255, 255, 255);}\n")

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

class Pantalla_Main_Menu(object):
	def setupUi(self, Dialog):
		#Esto hizo Agus a mano


		#Rellenar con urls de la BD
		#ESTO CAUSA DELAY EN LA APP
		print ("Cargando imagenes...")
		self.pixmap1=QPixmap()
		self.id_p1=None

		self.pixmap2=QPixmap()
		self.id_p2=None
		

		self.pixmap3=QPixmap()
		self.id_p3=None
		

		self.pixmap4=QPixmap()
		self.id_p4=None
		
		print ("Imagenes cargadas!")




		Dialog.setObjectName("QVer")
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

		#Anterior
		self.anteriores = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.anteriores.sizePolicy().hasHeightForWidth())
		self.anteriores.setSizePolicy(sizePolicy)
		self.anteriores.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../Images-UI/botonAnt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.anteriores.setIcon(icon)
		self.anteriores.setObjectName("anteriores")
		self.horizontalLayout.addWidget(self.anteriores)

		#SetPeli1
		self.peli1 = QLabelClickable()
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.peli1.sizePolicy().hasHeightForWidth())
		self.peli1.setSizePolicy(sizePolicy)
		self.peli1.setText("")
		self.peli1.setScaledContents(True)
		self.peli1.setObjectName("peli1")
		self.horizontalLayout.addWidget(self.peli1)

		#SetPeli2
		self.peli2 = QLabelClickable()
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.peli2.sizePolicy().hasHeightForWidth())
		self.peli2.setSizePolicy(sizePolicy)
		self.peli2.setText("")
		self.peli2.setScaledContents(True)
		self.peli2.setObjectName("peli2")
		self.horizontalLayout.addWidget(self.peli2)

		#SetPeli3
		self.peli3 = QLabelClickable()
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.peli3.sizePolicy().hasHeightForWidth())
		self.peli3.setSizePolicy(sizePolicy)
		self.peli3.setText("")
		self.peli3.setScaledContents(True)
		self.peli3.setObjectName("peli3")
		self.horizontalLayout.addWidget(self.peli3)

		#SetPeli4
		self.peli4 = QLabelClickable()
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.peli4.sizePolicy().hasHeightForWidth())
		self.peli4.setSizePolicy(sizePolicy)
		self.peli4.setText("")
		self.peli4.setScaledContents(True)
		self.peli4.setObjectName("peli4")
		self.horizontalLayout.addWidget(self.peli4)

		#Siguiente
		self.siguientes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.siguientes.sizePolicy().hasHeightForWidth())
		self.siguientes.setSizePolicy(sizePolicy)
		self.siguientes.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("../Images-UI/botonSig.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
		self.lbl_info.hide()
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
		self.lbl_stc.setGeometry(QtCore.QRect(133, 50, 250, 31))
		self.lbl_stc.setStyleSheet("font: 18pt \"Avengeance\";\n"
		"color: rgb(255, 255, 255);\n"
		"background-color: rgba(0, 0, 0,0%);")
		self.lbl_stc.setObjectName("lbl_stc")
		self.txt_usr = QtWidgets.QLineEdit(self.frame)
		self.txt_usr.setGeometry(QtCore.QRect(90, 200, 341, 51))
		font = QtGui.QFont()
		font.setFamily("Arial")
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
		self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
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

class Pantalla_Info(object):
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


		self.label = QLabelClickable(Dialog)

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