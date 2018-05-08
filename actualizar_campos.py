# -*- coding: utf-8 -*-
#Añadir campos:
#addAttributes() sobre el dataProvider de la capa. 
#updateFields() sobre la capa.
#Borrar campos:
#deleteAttributes() sobre el dataProvider de la capa. 
#updateFields() sobre la capa.
#Calcular valores:
#changeAttributeValues() sobre el dataProvider de la capa 
#updateFeature()
#IMPORTAMOS EL QVARIANT NECESARIO PARA CREAR UN CAMPO QgsField
from PyQt4.QtCore import QVariant
#CAPTURA COMO LAYER LA CAPA ACTIVA
layer= qgis.utils.iface.mapCanvas().currentLayer()
#ACCEDEMOS AL DATAPROVIDER Y CREAMOS LOS CAMPOS DE LA LISTA
layer.dataProvider().addAttributes( [ QgsField("NOMBRE", QVariant.String), QgsField("NUMERO", QVariant.Int) ] )
#ACTUALIZAMOS LA CAPA
layer.updateFields()
