layer = iface.activeLayer()
#convertimos a CSV con el método writeAsVectorFormat() de la Clase QgsVectorFileWriter
QgsVectorFileWriter.writeAsVectorFormat(layer, r"E:\CURSO_PYQGIS\CAPAS_PROCESADAS\capa_ciudades.csv", "utf-8", None, "CSV",layerOptions ='GEOMETRY=AS_WKT')
#cargar la cap en la TOC
uri = "file:///E:/CURSO_PYQGIS/CAPAS_PROCESADAS/capa_ciudades.csv?delimiter=%s&xField=%s&yField=%s" % (",", "LONGITUDE", "LATITUDE")
vlayer = QgsVectorLayer(uri, "capa ciudades csv", "delimitedtext")
QgsMapLayerRegistry.instance().addMapLayer(vlayer)

#para eliminar la capa de la TOC
QgsMapLayerRegistry.instance().removeMapLayer(vlayer.id())