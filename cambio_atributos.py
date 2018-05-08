# -*- coding: utf-8 -*-
from PyQt4.QtCore import QVariant
#IMPORTAMOS EL MODULO re PARA OPERAR CON LA CADENA DE TEXTO
import re
n=-1
#CAPTURAMOS COMO LAYER LA CAPA ACTIVA
layer= qgis.utils.iface.mapCanvas().currentLayer()
#OBTENEMOS LA COLECCION DE FEATURES
features = layer.getFeatures()
#RECORREMOS CADA ELEMENTO DE LA COLECCION
for feature in features:
    n=n+1
    #CAPTURAMOS EL VALOR DEL CAMPO NAME EN DOS VARIABLES
    nomRio = feature.attribute('NAME')
    numRio = feature.attribute('NAME')
    print nomRio
    #RECALCULAMOS LOS VALORES DE NOMBRE Y DE NUMERO A PARTIR DEL CAMPO
    nomRio = re.sub("\d", '', nomRio)
    print nomRio
    numRio = re.sub("\D", "", numRio)
    print numRio
     #INTRODUCIMOS LOS VALORES NUEVOS EN UN DICCIONARIO ORDEN_CAMPO:VALOR
    attrs = { 4 : nomRio, 5 : numRio }
     #CAMBIAMOS LOS VALORES DE LOS CAMPOS INDICADOS EN EL DICCIONARIO
    layer.dataProvider().changeAttributeValues({ n : attrs })