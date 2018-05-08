from PyQt4.QtCore import *
from PyQt4.QtGui import *

#COGE LA CAPA DE CARRETERAS COMO CAPA ACTIVA
layer = qgis.utils.iface.activeLayer()

# DEFINE VALOR, COLOR Y ETIQUETA
carreteras = {
    'Ferry Route': ('#f00', 'Ferry'),
    'Major Highway': ('#0f0', 'Principal'),
    'Secondary Highway': ('#ff0', 'Secundaria')}

# CREA UN DICICIONARIO CON LAS CATEGORIAS
categories = []

for carretera_tipo, (color, label) in carreteras.items():
    symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(color))
    category = QgsRendererCategoryV2(carretera_tipo, symbol, label)
    categories.append(category)

# CREA EL RENDERER Y SE LO ASIGNA A LA CAPA
expression = 'Type' # nombre del campo
renderer = QgsCategorizedSymbolRendererV2(expression, categories)
layer.setRendererV2(renderer)

#REFRESCA LA TOC
iface.mapCanvas().refresh()
qgis.utils.iface.legendInterface().refreshLayerSymbology(layer)
layer.triggerRepaint()
