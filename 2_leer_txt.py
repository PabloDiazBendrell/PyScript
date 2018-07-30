#-------------------------------------------------------------------------------
# Name:        2_Ingresar_NuevaImagen.py
# Purpose:     Permite agregar una nueva escena al repositorio satelital leyendo
#              la data de un txt.(id_imagen, cod_solicitud,geom, etc)
#
# Author:      Ing. Pablo Diaz Bendrell
# Email:       adiaz@sbn.gob.pe; diazbendrell.pablo@gmail.com
# Telefono:    952888911
# Created:     21/05/2018
# Copyright:   (c) adiaz 2018
# Licence:     GNU GPL
#-------------------------------------------------------------------------------
from os import listdir
import os
import psycopg2
from pprint import pprint
import sys
import re

## 1.- funcion que permite conectase a la base de datos e ingresar nueva informacion.
def Insertar(imagen):
    print imagen[3].split(" :	")[1].strip()
    conexion="host='localhost' dbname='postgis' user='postgres' password='40669465'"
    obj=psycopg2.connect(conexion)
    objcursor=obj.cursor()
##    query="INSERT INTO repositorio_imagenes_conida_cnois (id_imagen,oficio,combinacio,resolucion,formato,fecha_o,proceso,categoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" ,(imagen[0],imagen[1],'BUNDLE',0.7,'ECW','28/05/18','FUSIONADA','PENDIENTE POR RECIBIR')
    objcursor.execute("INSERT INTO repositorio_imagenes_conida_cnois (id_imagen,oficio,combinacio,resolucion,formato,fecha_o,proceso,categoria,geom)"
     "VALUES ('"+imagen[0]+"','"+imagen[1]+"','BUNDLE',0.7,'ECW','28/05/18','FUSIONADA','PENDIENTE POR RECIBIR',ST_GeomFromText('MULTIPOLYGON ((("+imagen[3].split(" :	")[1] +imagen[2].split(" :	")[1]+
     ","+imagen[5].split(" :	")[1] +imagen[4].split(" :	")[1]+","+imagen[7].split(" :	")[1] +imagen[6].split(" :	")[1]+","+ imagen[9].split(" :	")[1] +imagen[8].split(" :	")[1]+","+imagen[3].split(" :	")[1] +imagen[2].split(" :	")[1]+")))'))")
    obj.commit()

## 2.- Ruta donde se guarda el archivo txt que contiene la informacion satelital que quiere actualizar.
ruta='E:\\1_BACKUP IMAGENES DE SATELITE_NPprimario\\CONIDA-CNOIS\\2018\\JUNIO 2018\\img.txt'

## 3.- Ruta donde se guarda el archivo txt que contiene la informacion satelital que quiere actualizar.
f=open (ruta,'r')
linea=f.readlines()
imagen=[]
for i in range(0,len(linea)):
    imagen.append(linea[i].strip())
    print imagen[i]


Insertar(imagen)






