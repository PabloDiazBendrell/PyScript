#-------------------------------------------------------------------------------
# Name:        1_Calculo_Peso_Update.py
# Purpose:     Permite calcular el peso y el area de varias imagenes de satelite contenidas
#              en un directorio y actualiza la informacion de la base de datos.
#
# Author:      Ing. Pablo Diaz Bendrell
# Email:       adiaz@sbn.gob.pe; diazbendrell.pablo@gmail.com
# Telefono:    952888911
# Created:     12/05/2018
# Copyright:   (c) adiaz 2018
# Licence:     GNU GPL
#-------------------------------------------------------------------------------
from os import listdir
import os
import psycopg2
from pprint import pprint
import sys
import re

## 1.- funcion que permite conectase a la base de datos y actualizar la informacion de peso de la imagen.
def Actualizar(imagen,peso):
    conexion="host='localhost' dbname='postgis' user='postgres' password='40669465'"
    obj=psycopg2.connect(conexion)
    objcursor=obj.cursor()
    objcursor.execute("UPDATE repositorio_imagenes_conida_cnois SET categoria='SERVIDOR SBN',"+
    "area=(ST_area(ST_AsText(ST_Transform(ST_GeomFromText(st_astext((ST_Dump(geom)).geom),4326),32718))))/1000000,"+
    "peso="+str(peso)+" WHERE id_imagen='"+imagen+"'")

    obj.commit()
## 2.- Bucle para leer todo las archivos con extension ECW dentro un directorio para calcular su peso en Mb.
for i in listdir("E:\\1_BACKUP IMAGENES DE SATELITE_NPprimario\\CONIDA-CNOIS\\2018\\pendientes\\junio\\"):
    extension=i[-3:]
    if extension=="ecw":
        ## Almacena en un array los nombres de los archivos que cumple la condici?n
        imagen=i[0:len(i)-7]
        ## calcula el peso del archivo en byte
        peso=os.stat("E:\\1_BACKUP IMAGENES DE SATELITE_NPprimario\\CONIDA-CNOIS\\2018\\pendientes\\junio\\"+i).st_size
        ## calcula el peso del archivo en Megabyte
        peso=(peso/float(pow(1024,2)))
        ## Llama la funcion Actualizar enviando los parametros de actualziaci?n
        Actualizar(imagen,peso)














