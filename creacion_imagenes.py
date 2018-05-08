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
layers = iface.mapCanvas().layers()
for layer in layers:
    lst.append(layer.id())
renderer.setLayerSet(lst)
#fija el extent sobre el total de las capas
rect = QgsRectangle(renderer.fullExtent())
rect.scale(1.1)
renderer.setExtent(rect)
#output size
renderer.setOutputSize(img.size(), img.logicalDpiX())
#FIJA LA COMPOSICION FINAL Y CIERRA LA IMAGEN
renderer.render(p)
p.end()
#GENERA Y SALVA IMAGEN
img.save(pathToFile + "mi_primera_imagen" + "." + imageType ,imageType)
print "imagen generada"