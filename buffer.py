# -*- coding: utf-8 -*-
from qgis.analysis import *
dir(QgsGeometryAnalyzer)
#creamos la variable y recogemos la capa activa
layer= iface.activeLayer()
#nos aseguramos de que es ciudades
layer.name()
#hacemos un buffer
QgsGeometryAnalyzer().buffer(layer,r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_buff.shp',0.1)
#añadimos el resultado a la TOC
layer_buffer =QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_buff.shp','ciudades_buffer','ogr')
QgsMapLayerRegistry.instance().addMapLayer(layer_buffer)