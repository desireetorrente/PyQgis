# -*- coding: utf-8 -*-
#CAPTURA LA CAPA ACTIVA SU RENDERER Y SIMBOLO 
layer = qgis.utils.iface.activeLayer() 
renderer = layer.rendererV2() 
symbol = renderer.symbol() 
#CREA UN DICCIONARIO COPIANDO EL DICCIONARIO 
#DE LAS PROPIEDADES DEL SIMBOLO 
miDiccionario = symbol.symbolLayer(0).properties() 
miDiccionario
#CAMBIA EL VALOR DE LA CLAVE 'color'
miDiccionario ['color'] = '100,100,63,255'
miDiccionario
#CREA UN SIMBOLO DE PUNTO CON LAS PROPIEDADES DEL DICCIONARIO
miSimbolo = QgsFillSymbolV2.createSimple(miDiccionario)
#APLICA EL NUEVO SIMOLO A LA CAPA A TRAVES DEL RENDERER
renderer.setSymbol(miSimbolo)
#ACTUALIZA VISTA Y TOC 
iface.mapCanvas().refresh() 
qgis.utils.iface.legendInterface().refreshLayerSymbology(layer)
