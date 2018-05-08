#carga la capa de urbano en la TOC con una transparencia de 50%
layer = QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS\urbano.shp','urbano','ogr')
if not layer.isValid():
    print "la capa no es correcta"
QgsMapLayerRegistry.instance().addMapLayer(layer)

#consulto el campo de información

layer.displayField()

#cambio el campo

layer.setDisplayField ('FeatureCla')

#comprobar el cambio

layer.displayField()

