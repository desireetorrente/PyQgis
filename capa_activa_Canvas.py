#accedemos a la capa activa con CanvAS
cLayer = qgis.utils.iface.mapCanvas().currentLayer()
#imprimimos el nombre de la capa con el método.name
print cLayer.name()