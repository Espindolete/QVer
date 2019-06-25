#def validar() USUARIO:
from BDConnector import *
def verexist(dato):
    val=True
    for individuo in usuarios:
        if dato == individuo[1]:
            val=False
    return val

def validarcorreo(correo):
    def invalidchar(cadena):
        val=True
        caracteres = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m","_","0","1","2","3","4","5","6","7","8","9"]
        for x in cadena:
            if x in caracteres:
                pass
            else:
                val=False
        return val

    def invalidmail(cadena):
        val=True
        caracteres = ["gmail", "outlook", "hotmail", "icloud", "yahoo", "zoho", "gmx", "yandex", "mail", "lycos"]
        if cadena in caracteres:
            pass
        else:
            val=False
        return val

    def invalidcharname(cadena):
        val=True
        caracteres = ["-","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m","_","0","1","2","3","4","5","6","7","8","9"]
        for x in cadena:
            if x in caracteres:
                pass
            else:
                val=False
        return val

    def invalidomain(domain, domain2):
        val=True
        organ=domain
        pais=domain2
        if domain2 != "":
            if 1 < len(organ) < 10:
                val=invalidchar(organ)
                if val:
                    if 1 < len(pais) < 4:
                        val=invalidchar(pais)
                    else:
                        val=False
                else:
                    val=False
            else:
                val=False
            return val
        else:
            organ=domain
            if 1 < len(organ) < 10:
                val=invalidchar(organ)
            else:
                val=False
        return val
    
    val=False
    #Separar Correo
    try:
        fullmail=correo
        correo=correo.split("@")
        name=correo[0]
        backup=correo[1].split(".")
        mail=backup[0]
        domain=backup[1]
        if len(backup)==3:
            domain2=backup[2]
        else:
            domain2=""

        #lowers and uppers
        name=name.lower()

        #Validar pre @
        if len(name) == 0:
            val=False
        else:
            val=invalidcharname(name)
            if val:
                if 2 < len(mail):
                    val=invalidmail(mail)
                    if val:
                        val=invalidomain(domain, domain2)
                        val=exist(fullmail)
                else:
                    val=False
        '''
        print ("nombre de correo: ", name)
        print ("mail de correo: ", mail)
        print ("dominio de correo: ", domain)
        '''
    except Exception as e:
        pass
    return val

