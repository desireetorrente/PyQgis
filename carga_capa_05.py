from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

class CargaCapa:
    
    def __init__(self, iface):
        self.iface = iface

    def carga_capa (self,capa, nombre):
        layer = QgsVectorLayer(capa,nombre,'ogr')
        if not layer.isValid():
            print "la capa no es correcta"
        QgsMapLayerRegistry.instance().addMapLayer(layer)
    
    def da_transparencia(self):
        layer = self.iface.activeLayer()
        renderer = layer.rendererV2()
        symbol = renderer.symbol()
        symbol.setAlpha(0.5)
