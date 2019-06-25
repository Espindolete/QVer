import zipfile
import shutil, os

ruta = os.getcwd() + os.sep
zf=zipfile.ZipFile("fuentes.zip", "r")
for i in zf.namelist():
	print ("sucessfully")
	zf.extract(i, path="C:/Windows/Fonts")