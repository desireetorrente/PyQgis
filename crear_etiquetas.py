# -*- coding: utf-8 -*-
from PyQt4.QtGui import QColor
#SELECCIONA LA CAPA DE RIOS
layer=iface.activeLayer()
#CREA EL OBJETO DE ETIQUETA Y DETERMINA EL CAMPO A ETIQUETAR
palyr = QgsPalLayerSettings()
palyr.readFromLayer(layer)
palyr.enabled = True
palyr.fieldName = 'NOMBRE' #cuidado con nombre del campo
#PLACEMENT:
palyr.placement= QgsPalLayerSettings.Line
#COLOR:
palyr.textColor = QColor.fromRgb(49,195,255) #requiere importar QColor de PyQt4.QtGui
#TAMAÑO CON DEFINE PROPERTIES (EN MM)
palyr.setDataDefinedProperty(QgsPalLayerSettings.Size,True,True,'20','')
#PINTA LA ETIQUETA
palyr.writeToLayer(layer)
#REFRESCA EL MAPA Y LA TOC
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(layer)
layer.triggerRepaint()