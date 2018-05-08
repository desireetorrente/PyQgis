from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *


#carga la capa de urbano en la TOC con una transparencia de 50%
layer = QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS\urbano.shp','urbano','ogr')
if not layer.isValid():
    print "la capa no es correcta"
QgsMapLayerRegistry.instance().addMapLayer(layer)
renderer = layer.rendererV2()
symbol = renderer.symbol()
symbol.setAlpha(0.5)
