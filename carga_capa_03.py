from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

def carga_capa ():
    layer = QgsVectorLayer(r'E:\CURSO_PYQGIS\CAPAS\urbano.shp','urbano','ogr')
    if not layer.isValid():
        print "la capa no es correcta"
    QgsMapLayerRegistry.instance().addMapLayer(layer)

def da_transparencia():
    active_layer = iface.activeLayer ()
    renderer = active_layer.rendererV2 ()
    symbol = renderer.symbol ()
    symbol.setAlpha (0.5)
