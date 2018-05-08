# -*- coding: utf-8 -*-
#importar las funciones del procesamiento
import processing
#ahora necesitamos saber el algoritmo a usar
#para ello usamos el método alglist()
#si introduces alglist() te salen todos los métodos pero
#si pones entre los paréwntesis algún nombre, te hace el filtro
processing.alglist('difference')
processing.alghelp('qgis:difference')
#capas de entrada
layer_ciudades =r'E:\CURSO_PYQGIS\CAPAS\ciudades.shp'
layer_z_estudio = r'E:\CURSO_PYQGIS\CAPAS\zona_estudio.shp'
layer_ciudades_fuera = r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_fuera.shp'
#proceso:
processing.runalg('qgis:difference',layer_ciudades,layer_z_estudio,True,layer_ciudades_fuera)
#carga capa a la TOC:
layer_ciudades_fuera = QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_fuera.shp', 'layer_ciudades_fuera', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(layer_ciudades_fuera)