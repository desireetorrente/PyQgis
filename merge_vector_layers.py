# -*- coding: utf-8 -*-
#importar las funciones del procesamiento
import processing
#ahora necesitamos saber el algoritmo a usar
#para ello usamos el método alglist()
#si introduces alglist() te salen todos los métodos pero
#si pones entre los paréwntesis algún nombre, te hace el filtro
processing.alglist("merge")
#nos tiene que salir
#Merge vector layers---------------------------------->qgis:mergevectorlayers
#como ya sabemos lo que queremos usar
#usamos el método alghelp() para saber como es la sintaxis
processing.alghelp("qgis:mergevectorlayers")
#como ya sabemos la sintaxis, usamos ell sigueinte étodo
#para usar el algoritmo
#runalg(nombre del algoritmo,parámetro1,parámetro2,etc)
nom_layer_carret = r'E:\CURSO_PYQGIS\CAPAS\carreteras.shp'
nom_layer_rios = r'E:\CURSO_PYQGIS\CAPAS\rios.shp'
nom_resultado = r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\elementos_lineales.shp'
processing.runalg('qgis:mergevectorlayers', [nom_layer_carret, nom_layer_rios], nom_resultado)
layer_lineas = QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\elementos_lineales.shp', 'elem_lineal', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer (layer_lineas)