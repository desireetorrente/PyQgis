# -*- coding: utf-8 -*-
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from qgis.core import *
#TIPO DE IMAGEN Y DIRECTORIO DE SALIDA
imageType = "jpg"
pathToFile = "E:/CURSO_PYQGIS/"
# CREA Y CONFIGURA LA IMAGEN: SIZE, COLOR FONDO
img = QImage(QSize(800,600), QImage.Format_ARGB32_Premultiplied)
color = QColor(255,255,255)
img.fill(color.rgb())
# CREA EL PAINTER A PARTIR DE LA IMAGEN
p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)
#CONTENIDOS DE LA IMAGEN:
renderer = QgsMapRenderer()
lst = []
#lista las capas visibles, es iface y se cogen todas las capas
layers = iface.legendInterface().layers()
for layer in layers:
    if layer.name()<>'zona_estudio':
        lst.append(layer.id())
        
    elif layer.name()=='zona_estudio':
        iface.setActiveLayer(layer)
        rect = QgsRectangle(layer.extent())
#fija el extent sobre el total de las capas
renderer.setLayerSet(lst)
rect.scale(1.1)
renderer.setExtent(rect)
#output size
renderer.setOutputSize(img.size(), img.logicalDpiX())
#FIJA LA COMPOSICION FINAL Y CIERRA LA IMAGEN
renderer.render(p)
p.end()
#GENERA Y SALVA IMAGEN
img.save(pathToFile + "mi_segunda_imagen" + "." + imageType ,imageType)
print "imagen generada"