# -*- coding: utf-8 -*-
from qgis.analysis import *
layer = iface.activeLayer()
layer.name()
QgsGeometryAnalyzer().dissolve(layer,r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\carreteras_diss.shp',False,2)
layer_diss =QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\carreteras_diss.shp','carreteras_diss','ogr')
QgsMapLayerRegistry.instance().addMapLayer(layer_diss)