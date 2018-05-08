# -*- coding: utf-8 -*-
from qgis.analysis import *
layer = iface.activeLayer()
layer.name()
QgsGeometryAnalyzer().centroids(layer,r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\zonaest_centr.shp')
layer_centr =QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\zonaest_centr.shp','zonaest_centr','ogr')
QgsMapLayerRegistry.instance().addMapLayer(layer_centr)