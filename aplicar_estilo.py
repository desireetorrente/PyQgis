# -*- coding: utf-8 -*-
#aplicar estilo a otra capa
layer = iface.activeLayer()
layer.loadNamedStyle(r'E:\CURSO_PYQGIS\CAPAS_PROCESADAS\urbano.qml')
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(layer)
layer.triggerRepaint()