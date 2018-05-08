# -*- coding: utf-8 -*-
#accedemos a la capa actual
layer=qgis.utils.iface.mapCanvas().currentLayer()
#con getFeatures() accedemos a los elementos de la capa
#getFeature es de la clase QgsVectorLayer
features = layer.getFeatures()
#recorremos cada elementeo de la capa y decimos que lo imprima
for feature in features:
    print feature.attributes()