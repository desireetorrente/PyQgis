# -*- coding: utf-8 -*-
canvas = qgis.utils.iface.mapCanvas()
layer=qgis.utils.iface.mapCanvas().currentLayer()
features = layer.getFeatures()
for feature in layer.getFeatures(): 
    if feature.attribute('NAME') == 'Austin': 
        layer.setSelectedFeatures([feature.id()]) 
        canvas.panToSelected()