# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

pathToFile = r"E:/CURSO_PYQGIS/mi_segundo_mapa.pdf"

#CREA COMPOSICION
mapRenderer = iface.mapCanvas().mapRenderer()
c = QgsComposition(mapRenderer)
c.setPlotStyle(QgsComposition.Print)

#CONTENIDOS 
x, y = 30, 30
w, h = 220,220
composerMap = QgsComposerMap(c, x,y,w,h)

#le damos la escala
composerMap.setNewScale(5000000)
print composerMap.scale()
c.addItem(composerMap)
#titulo
composerLabel = QgsComposerLabel(c)
composerLabel.setText("Mi SEGUNDO MAPA")
composerLabel.adjustSizeToText()
composerLabel.setItemPosition(140,10)
c.addItem(composerLabel)
#leyenda
legend = QgsComposerLegend(c)
legend.model().setLayerSet(mapRenderer.layerSet())
c.addItem(legend)
legend.setItemPosition(c.paperWidth()-40, c.paperHeight()-55)
#escala
scale = QgsComposerScaleBar(c)
scale.setStyle('Numeric')
scale.setComposerMap(composerMap)
scale.applyDefaultSize()
c.addItem(scale)
scale.setItemPosition(10,c.paperHeight()-10)

#NORTE
ini = QPointF(10,20)
fin= QPoint(10,10)
arrow = QgsComposerArrow(ini,fin,c)
c.addItem(arrow)
#PRINTER
printer = QPrinter()
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName(pathToFile)
printer.setPaperSize(QSizeF(c.paperWidth(), c.paperHeight()), QPrinter.Millimeter)
printer.setFullPage(True)
printer.setColorMode(QPrinter.Color)
printer.setResolution(c.printResolution())

pdfPainter = QPainter(printer)
paperRectMM = printer.pageRect(QPrinter.Millimeter)
paperRectPixel = printer.pageRect(QPrinter.DevicePixel)
c.render(pdfPainter, paperRectPixel, paperRectMM)
pdfPainter.end()

print 'mapa generado'

