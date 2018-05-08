# -*- coding: utf-8 -*-
layer = qgis.utils.iface.activeLayer()
renderer = layer.rendererV2()
symbol = renderer.symbol() 
symbol.setSize(5)

#refrescamos el mapa para que se vuelva a mostrar con los cambios
iface.mapCanvas().refresh()
qgis.utils.iface.legendInterface().refreshLayerSymbology(layer)
