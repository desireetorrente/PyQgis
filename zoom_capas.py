# -*- coding: utf-8 -*-
canvas = iface.mapCanvas()
#opciones de zoomByFactorcanvas.zoomToFullExtent()
#canvas. zoomIn()
#canvas.zoomOut()
#canvas. zoomToPreviousExtent()
layer = iface.activeLayer()
layer.selectAll()
canvas.zoomToSelected()
layer.removeSelection()
