# -*- coding: utf-8 -*-
from PyQt4.QtGui import QColor

layer=iface.activeLayer()
#CREA EL OBJETO DE ETIQUETA Y DETERMINA EL CAMPO A ETIQUETAR
palyr = QgsPalLayerSettings()
palyr.readFromLayer(layer)
palyr.enabled = True
palyr.fieldName = 'NAME' #cuidado con nombre del campo
#PLACEMENT:
palyr.placement= QgsPalLayerSettings.OverPoint
#TAMAÑO
palyr.setDataDefinedProperty(QgsPalLayerSettings.Size,True,True,'10','')
#NEGRITA Y COLOR
palyr.setDataDefinedProperty(QgsPalLayerSettings.Bold,True,True,'1','')
palyr.setDataDefinedProperty(QgsPalLayerSettings.Color,True,False,'','COLOR')

#PINTA LA ETIQUETA
palyr.writeToLayer(layer)
#REFRESCA EL MAPA Y LA TOC
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(layer)
layer.triggerRepaint()