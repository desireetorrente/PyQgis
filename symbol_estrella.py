# -*- coding: utf-8 -*-
#renderer de la capa activa
layer=iface.activeLayer() 
renderer=layer.rendererV2()

#creamos los dos simbolos
symbol1 = QgsMarkerSymbolV2.createSimple({'name':'circle','color':'blue','size':'10'})
symbol2 = QgsMarkerSymbolV2.createSimple({'name':'star','color':'#9ecae1','size':'8'})

#symbolo layer y lo añadimos al primero
layerSymbol2= symbol2.symbolLayer(0)
symbol1.appendSymbolLayer(layerSymbol2)

#aplicamos el simbolo a la capa activa y cargamos
renderer.setSymbol(symbol1)
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(layer)
layer.triggerRepaint()