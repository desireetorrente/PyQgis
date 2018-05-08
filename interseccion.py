# -*- coding: utf-8 -*-
from qgis.analysis import *
layer_ciud =QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_buff.shp','ciudades_buff','ogr')
layer_zonaest =QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS\zona_estudio.shp','zona_estudio','ogr')
QgsOverlayAnalyzer().intersection(layer_ciud,layer_zonaest,r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_estudio.shp')
layer_ciud_est=QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_estudio.shp','ciudades_estudio','ogr')
QgsMapLayerRegistry.instance().addMapLayer(layer_ciud_est)