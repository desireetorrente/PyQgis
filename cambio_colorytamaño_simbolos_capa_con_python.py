# -*- coding: utf-8 -*-
#CREA UN SIMBOLO Y DA VALORES DE EXPRESSION 
symbol = QgsMarkerSymbolV2.createSimple({'name':'star','color_expression':'COLOR','size_expression':'SIZE'})
#ACCEDE AL RENDERER DE LA CAPA ACTIVA 
layer=iface.activeLayer() 
renderer=layer.rendererV2() 
#OTORGA AL RENDERER EL SIMBOLO CREADO 
renderer.setSymbol(symbol)
#REFRESCA VISTA Y TOC 
iface.mapCanvas().refresh() 
iface.legendInterface().refreshLayerSymbology(layer) 
#-repintamos el simbolo
layer.triggerRepaint()