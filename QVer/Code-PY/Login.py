


'''

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
'''




'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''