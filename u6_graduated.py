from PyQt4.QtCore import *
from PyQt4.QtGui import *

#COGE LA CAPA CIUDADES COMO CAPA ACTIVA
layer = qgis.utils.iface.activeLayer()

# DEFINE RANGOS, ETIQUETA, VALOR MAX Y MIN Y COLOR
rangos= (
    ('muy_baja', 2284, 2249213, 'white'),
    ('baja', 2249213, 4496142, 'yellow'),
    ('media',4496142, 6743071, 'orange'),
    ('alta', 6743071, 8990001, 'red')
   )

# CAPTURA LOS RANGOS
ranges = []
for label, lower, upper, color in rangos:
    symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(color))
    rng = QgsRendererRangeV2(lower, upper, symbol, label)
    ranges.append(rng)

# APLICA EL RENDERER A LA CAPA
expression = 'POP_MAX' # nombre del campo
renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
layer.setRendererV2(renderer)

#REFRESCA LA TOC
iface.mapCanvas().refresh()
qgis.utils.iface.legendInterface().refreshLayerSymbology(layer)
layer.triggerRepaint()