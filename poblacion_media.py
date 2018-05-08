# -*- coding: utf-8 -*-
#CAPTURA COMO LAYER LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer()
#CAPTURA EN LA VARIABLE N EL NUMERO DE ELEMENTOS
n = layer.featureCount()
print n
#CREA UNA VARIABLE EN LA QUE IR SUMANDO LA POBLACION
pob_tot = 0
#OBTIENEMOS LA COLECCION DE FEATURES DE LA CAPA
features = layer.getFeatures()
#RECORRE CADA ELEMENTO DE LA COLECCION
for feature in features:
    #ACCEDE AL DATO DE POBLACION DEL CAMPO POP_MAX
    print feature.attribute('POP_MAX')
    #SUMA A LA VARIABLE POP_TOT LA CIFRA CAPTURADA
    pob_tot = pob_tot + feature.attribute('POP_MAX')
#SUMA TOTAL DE LA POB Y POB MEDIA DIVIDIENDO ENTRE NUM REGISTROS
print pob_tot
pob_med = pob_tot/n
print pob_med

