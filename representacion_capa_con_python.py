# -*- coding: utf-8 -*-
#para ver el tipo de renderizado y su representación usamos:
#type() y dump()
layer = qgis.utils.iface.activeLayer()
renderer = layer.rendererV2()
print renderer.type()
print renderer.dump()
#en casos del tipo single podemos acceder a la
#simbologia a través del renderer
symbol = renderer.symbol() 
print symbol
print symbol.dump()
print symbol.color()
print symbol.color().name() 
print symbol.symbolLayerCount() 
print symbol.symbolLayer(0).properties()